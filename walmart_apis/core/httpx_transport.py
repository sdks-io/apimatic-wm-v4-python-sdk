"""httpx-backed transports -- the default implementations of the two transport protocols.

The sync and async adapters live together because they are peers differing only in ``await``, the
same reason :class:`RawClient` and :class:`AsyncRawClient` share a module. Everything httpx-specific
is confined here: swapping HTTP libraries means writing one more module like this one, not touching
anything else.

File ownership is written down here and nowhere else: every handle this module opens for a body --
a ``Path`` in a multipart part or a raw body -- is registered on the send's ``ExitStack``, so it is
closed when the send returns or raises, deterministically and never by a finalizer. A handle the
caller opened is passed through untouched and never closed."""

from __future__ import annotations

import asyncio
import inspect
import ssl
from collections.abc import AsyncIterable, AsyncIterator, Callable, Iterable, Iterator, Mapping
from contextlib import ExitStack
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import httpx
from typing_extensions import TypeIs

from .bodies import (
    BinaryBody,
    FormBody,
    JsonBody,
    MultipartBody,
    MultipartFile,
    MultipartPart,
    MultipartText,
    TextBody,
)
from .files import AsyncBinaryInput, AsyncBinaryReader, BinaryReader, FileContent
from .transport import (
    AsyncHttpClient,
    AsyncStreamedResponse,
    HttpClient,
    HttpRequest,
    HttpResponse,
    StreamedResponse,
)

_DEFAULT_TIMEOUT = 30.0

_CHUNK_SIZE = 65_536
"""httpx's own multipart chunk size (``FileField.CHUNK_SIZE``), matched for the raw-body readers."""


def _is_async_reader(content: object) -> TypeIs[AsyncBinaryReader]:
    """Whether ``content`` is a reader whose ``read`` must be awaited.

    ``isinstance`` alone cannot tell the two reader protocols apart -- ``runtime_checkable``
    checks only that ``read`` exists -- so the async arm is decided by whether ``read`` is a
    coroutine function. ``TypeIs`` rather than ``TypeGuard``: the negative branch must narrow
    too, or the sync adapter could not prove its return type."""
    return isinstance(content, AsyncBinaryReader) and inspect.iscoroutinefunction(getattr(type(content), "read", None))


def _require_binary_reader(reader: BinaryReader) -> None:
    """Reject a text-mode handle before its first chunk reaches the wire.

    ``read(0)`` returns ``b""`` for a binary handle and ``""`` for a text one, without consuming
    anything -- a one-sided check: only ``str`` raises (``RawIOBase`` may legally return ``None``).

    Raises:
        TypeError: If ``reader`` was opened in text mode."""
    if isinstance(reader.read(0), str):
        raise TypeError("a text-mode file cannot carry binary content -- open it in binary mode ('rb')")


def _sync_content(content: AsyncBinaryInput, stack: ExitStack) -> bytes | BinaryReader | Iterable[bytes]:
    """Adapt a raw-body descriptor for the sync client, opening what needs opening onto ``stack``.

    Takes the full async union because that is ``BinaryBody.content``'s type -- the *static* gate
    is the emitted endpoint signature, which offers the sync client only the sync arms. The
    rejection below is the runtime backstop for a caller no checker saw, replacing the opaque
    stream-type error the underlying library would raise mid-send.

    A reader is handed on **only when it is also iterable**. The library's ``content=`` gate is
    ``isinstance(..., Iterable)`` and it prefers ``read`` only once past it, so a reader carrying
    nothing but ``read`` -- all the protocol asks for -- would be refused there; it is chunked here
    instead. The passthrough is what lets the library size a real file into a ``Content-Length``
    rather than falling back to chunked.

    Raises:
        TypeError: If ``content`` is an async arm, or a reader opened in text mode."""

    def chunks(reader: BinaryReader) -> Iterator[bytes]:
        while chunk := reader.read(_CHUNK_SIZE):
            yield chunk

    if isinstance(content, (bytes, bytearray)):
        return bytes(content)
    if isinstance(content, Path):
        return stack.enter_context(content.open("rb"))
    if _is_async_reader(content) or isinstance(content, AsyncIterable):
        raise TypeError(
            "an async byte source cannot be sent by the sync client -- pass bytes, a Path, "
            "a binary reader or an Iterable[bytes], or use the async client"
        )
    if isinstance(content, BinaryReader):
        _require_binary_reader(content)
        return content if isinstance(content, Iterable) else chunks(content)
    return content


def _async_content(content: AsyncBinaryInput, stack: ExitStack) -> bytes | AsyncIterable[bytes]:
    """Adapt a raw-body descriptor to the async byte stream the async client demands.

    Sync arms read through a worker thread so a large upload from a slow disk does not park the
    event loop; the two async arms are consumed natively. A ``Path`` is opened here, eagerly, onto
    ``stack`` -- a momentary open on the loop, exactly as the multipart leg's ``_open`` does -- so
    a mid-send failure closes it on the stack's unwind rather than at a finalizer.

    The arm order is load-bearing: readers before iterables (a file handle iterates by *lines*),
    the async-reader guard before ``AsyncIterable`` (an async file is async-iterable by lines),
    and ``bytes`` before everything (it is an ``Iterable[int]``).

    Raises:
        TypeError: If ``content`` is a reader opened in text mode."""

    async def threaded_chunks(reader: BinaryReader) -> AsyncIterator[bytes]:
        # Every read in a worker thread: the non-blocking property of the async raw-body leg.
        while chunk := await asyncio.to_thread(reader.read, _CHUNK_SIZE):
            yield chunk

    async def awaited_chunks(reader: AsyncBinaryReader) -> AsyncIterator[bytes]:
        while chunk := await reader.read(_CHUNK_SIZE):
            yield chunk

    async def iterable_chunks(chunks: Iterable[bytes]) -> AsyncIterator[bytes]:
        # Pulled on the loop: a caller's generator is the caller's own code; one that must not
        # block the loop is passed as an AsyncIterable instead.
        for chunk in chunks:
            yield chunk

    if isinstance(content, (bytes, bytearray)):
        return bytes(content)
    if isinstance(content, Path):
        return threaded_chunks(stack.enter_context(content.open("rb")))
    if _is_async_reader(content):
        return awaited_chunks(content)
    if isinstance(content, BinaryReader):
        _require_binary_reader(content)
        return threaded_chunks(content)
    if isinstance(content, AsyncIterable):
        return content
    return iterable_chunks(content)


def _open(content: FileContent, stack: ExitStack) -> bytes | BinaryReader:
    """Resolve a multipart part's content descriptor, opening what needs opening onto ``stack``.

    The one place the ownership rule is written down in code: a ``Path``'s handle is the SDK's,
    registered on the stack and closed when the send returns or raises; a caller's handle is
    returned untouched and never closed.

    Raises:
        TypeError: If ``content`` is a reader opened in text mode."""
    if isinstance(content, (bytes, bytearray)):
        return bytes(content)
    if isinstance(content, Path):
        return stack.enter_context(content.open("rb"))
    _require_binary_reader(content)
    return content


def _httpx_part(part: MultipartPart, stack: ExitStack) -> tuple[str, Any]:
    """Render one part in httpx's ``files=`` tuple spelling.

    Text parts go through the *file* spelling -- ``(None, text)``, a part with no filename --
    rather than through ``data=``, because httpx chooses the encoding on the **truthiness** of
    ``files``: an operation declaring ``multipart/form-data`` with no binary part would otherwise
    be sent as ``application/x-www-form-urlencoded``. The rendered bytes are identical either way,
    repeated keys and name escaping included, so the invariant costs nothing."""
    match part:
        case MultipartText(name, text, None):
            return (name, (None, text))
        case MultipartText(name, text, media_type):
            return (name, (None, text, media_type))
        case MultipartFile(name, content, filename, media_type):
            return (name, (filename, _open(content, stack), media_type))


def _body_kwargs(
    request: HttpRequest, stack: ExitStack, *, binary_content: Callable[[AsyncBinaryInput, ExitStack], object]
) -> dict[str, Any]:
    """Map the request's body -- and the headers that describe it -- onto httpx's keywords.

    This ``match`` is the only place the body union is interpreted, and it is exhaustive by
    construction: adding a body shape without handling it here is a type error.

    Nothing here spells a media type or a charset. A body that has one carries it, written at the
    endpoint from the operation's content key, and it is merged **underneath** the request's own
    headers so a caller's ``extra_headers`` still wins -- the precedence httpx gives its own derived
    headers. A text body is encoded with the charset it declares and labelled with that same field,
    so the bytes and the label cannot disagree. The two arms that carry none are the two whose media
    type belongs to the encoder: url-encoded is fixed by the ``data=`` keyword, and multipart's
    boundary exists only once httpx has minted it. That is why headers travel out of this function
    rather than beside it.

    ``binary_content`` is the one flavour-differing arm, passed as data with no default so each
    transport must name its own adapter -- ``_sync_content`` or ``_async_content``. One shared
    match rather than two sibling copies: this module is hand-written, where five duplicated arms
    to differ in one is drift risk rather than generator output.

    Args:
        request: The request whose body and headers are being mapped.
        stack: The send's exit stack, onto which any handle opened for this body is registered.
        binary_content: The flavour's raw-body adapter.

    Returns:
        The httpx keyword arguments carrying this body, ``headers`` among them."""
    match request.body:
        case None:
            return {"headers": request.headers}
        case JsonBody(None, media_type):
            # ``json=None`` is indistinguishable to httpx from no ``json`` argument at all, so the
            # body would vanish rather than going out as the four bytes the caller asked for.
            # ``content=`` is the only keyword that will carry them.
            return {"headers": {"content-type": media_type, **request.headers}, "content": b"null"}
        case JsonBody(value, media_type):
            return {"headers": {"content-type": media_type, **request.headers}, "json": value}
        case FormBody(fields):
            return {"headers": request.headers, "data": fields}
        case MultipartBody(parts):
            return {"headers": request.headers, "files": [_httpx_part(part, stack) for part in parts]}
        case BinaryBody(content, media_type):
            return {
                "headers": {"content-type": media_type, **request.headers},
                "content": binary_content(content, stack),
            }
        case TextBody(text, media_type, charset):
            return {
                "headers": {"content-type": f"{media_type}; charset={charset}", **request.headers},
                "content": text.encode(charset),
            }


def _timeout_kwargs(request: HttpRequest) -> dict[str, Any]:
    """Map a per-request timeout onto httpx's keyword, or contribute nothing.

    Omitting is deliberate rather than passing ``timeout=None``: to httpx that means *no timeout at
    all*, not *use the client's own*, so an absent override must not reach the call.

    Args:
        request: The request whose ``timeout`` is being mapped.

    Returns:
        ``{"timeout": ...}`` when the request set one, otherwise an empty mapping."""
    return {} if request.timeout is None else {"timeout": httpx.Timeout(request.timeout)}


@dataclass(frozen=True, slots=True)
class _HttpxStreamedResponse:
    """A thin veneer meeting :class:`StreamedResponse` over the library's own response.

    httpx lowercases header names on iteration, so ``headers`` meets the protocols' casing
    obligation by construction; ``read`` is the library's own, which both buffers the body and
    releases the connection -- the exact obligation the protocol states."""

    _response: httpx.Response

    @property
    def status_code(self) -> int:
        return self._response.status_code

    @property
    def headers(self) -> Mapping[str, str]:
        return dict(self._response.headers)

    def iter_bytes(self, chunk_size: int) -> Iterator[bytes]:
        return self._response.iter_bytes(chunk_size)

    def read(self) -> bytes:
        return self._response.read()

    def close(self) -> None:
        self._response.close()


@dataclass(frozen=True, slots=True)
class _AsyncHttpxStreamedResponse:
    """The awaited twin of :class:`_HttpxStreamedResponse`, meeting :class:`AsyncStreamedResponse`."""

    _response: httpx.Response

    @property
    def status_code(self) -> int:
        return self._response.status_code

    @property
    def headers(self) -> Mapping[str, str]:
        return dict(self._response.headers)

    def aiter_bytes(self, chunk_size: int) -> AsyncIterator[bytes]:
        return self._response.aiter_bytes(chunk_size)

    async def aread(self) -> bytes:
        return await self._response.aread()

    async def aclose(self) -> None:
        await self._response.aclose()


class HttpxClient(HttpClient):
    """Sync transport backed by httpx.

    Uses connection pooling via a single ``httpx.Client``, and returns buffered responses.

    Requests honour the standard proxy and TLS environment variables -- ``HTTP_PROXY`` /
    ``HTTPS_PROXY`` / ``ALL_PROXY`` / ``NO_PROXY`` (consulted only when ``proxy_url`` is unset) and
    ``SSL_CERT_FILE`` / ``SSL_CERT_DIR`` (the trust store). That is the underlying library's default
    rather than a decision made here, and it is stated because it is request behaviour the
    environment can change; a caller needing it off supplies a transport of their own.

    ``verify`` takes an ``ssl.SSLContext`` as well as a bool: a private CA bundle or a client
    certificate is configured by building one (``ssl.create_default_context(cafile=...)``), which is
    the one spelling the pinned library still supports for either."""

    def __init__(
        self,
        *,
        timeout: float = _DEFAULT_TIMEOUT,
        proxy_url: str | None = None,
        verify: ssl.SSLContext | bool = True,
    ) -> None:
        self._client = httpx.Client(
            proxy=proxy_url,
            timeout=httpx.Timeout(timeout),
            verify=verify,
        )
        self._closed = False

    def send(self, request: HttpRequest) -> HttpResponse:
        # The stack owns every handle opened for this body; a buffered send has fully consumed the
        # body by the time the response returns, so closing on exit is correct -- and an exception
        # mid-send closes on the unwind.
        with ExitStack() as stack:
            response = self._client.request(
                method=request.method,
                url=request.url,
                **_timeout_kwargs(request),
                **_body_kwargs(request, stack, binary_content=_sync_content),
            )

        return HttpResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            content=response.content,
            request=request,
        )

    def stream(self, request: HttpRequest) -> StreamedResponse:
        # The stack closes once the head has arrived -- which is after the request body has been
        # sent in full, so closing there is correct, not early. The *response* body is pending;
        # the returned wrapper owns that connection until it is closed.
        with ExitStack() as stack:
            httpx_request = self._client.build_request(
                method=request.method,
                url=request.url,
                **_timeout_kwargs(request),
                **_body_kwargs(request, stack, binary_content=_sync_content),
            )
            response = self._client.send(httpx_request, stream=True)
        return _HttpxStreamedResponse(response)

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        self._client.close()


class AsyncHttpxClient(AsyncHttpClient):
    """Async transport backed by httpx.

    Uses connection pooling via a single ``httpx.AsyncClient``, and returns buffered responses.

    Requests honour the standard proxy and TLS environment variables -- ``HTTP_PROXY`` /
    ``HTTPS_PROXY`` / ``ALL_PROXY`` / ``NO_PROXY`` (consulted only when ``proxy_url`` is unset) and
    ``SSL_CERT_FILE`` / ``SSL_CERT_DIR`` (the trust store). That is the underlying library's default
    rather than a decision made here, and it is stated because it is request behaviour the
    environment can change; a caller needing it off supplies a transport of their own.

    ``verify`` takes an ``ssl.SSLContext`` as well as a bool: a private CA bundle or a client
    certificate is configured by building one (``ssl.create_default_context(cafile=...)``), which is
    the one spelling the pinned library still supports for either."""

    def __init__(
        self,
        *,
        timeout: float = _DEFAULT_TIMEOUT,
        proxy_url: str | None = None,
        verify: ssl.SSLContext | bool = True,
    ) -> None:
        self._client = httpx.AsyncClient(
            proxy=proxy_url,
            timeout=httpx.Timeout(timeout),
            verify=verify,
        )
        self._closed = False

    async def send(self, request: HttpRequest) -> HttpResponse:
        with ExitStack() as stack:
            response = await self._client.request(
                method=request.method,
                url=request.url,
                **_timeout_kwargs(request),
                **_body_kwargs(request, stack, binary_content=_async_content),
            )

        return HttpResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            content=response.content,
            request=request,
        )

    async def stream(self, request: HttpRequest) -> AsyncStreamedResponse:
        with ExitStack() as stack:
            httpx_request = self._client.build_request(
                method=request.method,
                url=request.url,
                **_timeout_kwargs(request),
                **_body_kwargs(request, stack, binary_content=_async_content),
            )
            response = await self._client.send(httpx_request, stream=True)
        return _AsyncHttpxStreamedResponse(response)

    async def aclose(self) -> None:
        if self._closed:
            return
        self._closed = True
        await self._client.aclose()
