"""The HTTP boundary: what a request and a response are, and what a transport must provide.

The two protocols are the seam between the SDK and whatever HTTP library actually moves bytes.
Keeping them SDK-owned is deliberate: ``ApiResult.response`` hands an :class:`HttpResponse` back to
callers, so no third-party request/response type reaches the public surface, and a caller can supply
their own transport by satisfying :class:`HttpClient` or :class:`AsyncHttpClient`.

The request and response shapes live here; the body shapes a request can carry live in
``bodies.py``, beside the factories that build them, and reach a transport through
:attr:`HttpRequest.body`."""

from __future__ import annotations

import json
from collections.abc import AsyncIterator, Iterator, Mapping
from dataclasses import dataclass
from typing import Any, Protocol

from .bodies import RequestBody


@dataclass(frozen=True, slots=True)
class HttpRequest:
    """An outbound request, fully resolved and ready for a transport to send."""

    method: str
    url: str
    headers: Mapping[str, str]

    body: RequestBody | None = None
    timeout: float | None = None
    """Seconds to wait, or ``None`` to leave the transport's own timeout in force."""


@dataclass(frozen=True, slots=True)
class HttpResponse:
    """A buffered response. ``content`` is the raw body; decoding is the caller's choice.

    On the success branch of a *streamed* call ``content`` is empty, deliberately: the body is the
    payload there, carried unread by the streamed response instead of buffered here."""

    status_code: int
    headers: Mapping[str, str]
    """Header names lowercased, per the transports' obligation -- look keys up in lowercase."""

    content: bytes = b""
    request: HttpRequest | None = None

    def text(self, encoding: str = "utf-8", errors: str = "replace") -> str:
        """Decode the body as text, mirroring :meth:`bytes.decode`.

        Undecodable bytes are replaced by default, because the caller this serves is a diagnostic
        one -- rendering an error body into a log line, where raising would lose the little
        information there is. The payload path passes ``errors="strict"`` instead, so a body that
        is not what it claims raises rather than arriving with ``\\ufffd`` standing in for it.

        Args:
            encoding: Character encoding to decode with.
            errors: How to handle undecodable bytes, as ``bytes.decode`` takes it.

        Returns:
            The body decoded as text.

        Raises:
            UnicodeDecodeError: Only when ``errors="strict"`` is passed."""
        return self.content.decode(encoding, errors=errors)

    def json(self) -> Any:
        """Parse the body as JSON, or raise ``ValueError``.

        Parsed from ``content`` rather than from :meth:`text`, so RFC 8259 encoding detection
        applies (UTF-8/16/32, BOM-tolerant) and an undecodable byte is a failure rather than a
        replacement character smuggled into a successful payload.

        Returns:
            Whatever the body parses to -- an object, array or scalar.

        Raises:
            ValueError: If the body is not valid JSON, or is not decodable at all."""
        try:
            return json.loads(self.content)
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            raise ValueError("Response body is not valid JSON") from e


class StreamedResponse(Protocol):
    """A response whose head has arrived and whose body has not been read.

    The status and headers are facts as soon as this exists, which is what lets a streamed call
    still yield a ``Success`` or a ``Failure``: only the payload is deferred, never the outcome.
    It holds a connection until it is closed. Header names MUST be lowercased, exactly as on
    :class:`HttpResponse`.

    ``read`` is the error path's seam, not a convenience over ``iter_bytes``: it must both buffer
    the whole body *and* release the connection, so an error body survives the close that frees
    the socket."""

    @property
    def status_code(self) -> int: ...

    @property
    def headers(self) -> Mapping[str, str]: ...

    def iter_bytes(self, chunk_size: int) -> Iterator[bytes]: ...

    def read(self) -> bytes: ...

    def close(self) -> None: ...


class AsyncStreamedResponse(Protocol):
    """The awaited twin. ``aclose`` rather than ``close``, matching the SDK's async client.

    ``status_code`` and ``headers`` stay synchronous properties -- the head has already arrived.
    Header names MUST be lowercased, exactly as on :class:`HttpResponse`, and ``aread`` carries
    ``read``'s obligation: buffer the whole body and release the connection."""

    @property
    def status_code(self) -> int: ...

    @property
    def headers(self) -> Mapping[str, str]: ...

    def aiter_bytes(self, chunk_size: int) -> AsyncIterator[bytes]: ...

    async def aread(self) -> bytes: ...

    async def aclose(self) -> None: ...


class HttpClient(Protocol):
    """Sync transport contract.

    The contract deliberately carries **two** request seams: ``send`` returns a buffered response,
    and ``stream`` returns one whose body has not been read. A caller-supplied transport must
    implement both -- the accepted cost, stated in ADR-0046, of keeping streamed downloads on the
    same ``ApiResult`` surface as everything else.

    Implementations:
    - MUST NOT mutate the incoming :class:`HttpRequest`.
    - MUST honour ``request.timeout`` when it is set, and fall back to their own configured
      timeout when it is ``None``.
    - MUST lowercase the header names on the returned :class:`HttpResponse`: HTTP/1.1 treats them
      case-insensitively and HTTP/2 requires lowercase, so a caller's lookup needs no case
      handling -- the same rule, for the same reason, as the request side in
      ``_internal/headers.py``. A :class:`StreamedResponse`'s ``headers`` carry the same
      obligation.
    - SHOULD be idempotent for ``close()``.
    - MAY raise their underlying library's exceptions."""

    def send(self, request: HttpRequest) -> HttpResponse:
        """Execute a request and return a buffered response.

        Args:
            request: The request to send, which MUST NOT be mutated.

        Returns:
            The response, fully buffered, with its header names lowercased."""
        ...

    def stream(self, request: HttpRequest) -> StreamedResponse:
        """Execute a request and return its response with the body unread.

        Returns once the response head has arrived; the connection stays checked out until the
        returned response is closed.

        Args:
            request: The request to send, which MUST NOT be mutated.

        Returns:
            The response head, its body pending, its header names lowercased."""
        ...

    def close(self) -> None:
        """Release underlying resources (connections, pools). Should be idempotent."""
        ...


class AsyncHttpClient(Protocol):
    """Async transport contract -- the same shape as :class:`HttpClient`, awaited.

    The same obligations apply, including honouring ``request.timeout``, lowercasing the
    response's header names, and carrying both request seams. ``aclose`` rather than ``close``
    matches httpx and the SDK's own async client."""

    async def send(self, request: HttpRequest) -> HttpResponse:
        """Execute a request and return a buffered response.

        Args:
            request: The request to send, which MUST NOT be mutated.

        Returns:
            The response, fully buffered, with its header names lowercased."""
        ...

    async def stream(self, request: HttpRequest) -> AsyncStreamedResponse:
        """Execute a request and return its response with the body unread.

        Returns once the response head has arrived; the connection stays checked out until the
        returned response is closed.

        Args:
            request: The request to send, which MUST NOT be mutated.

        Returns:
            The response head, its body pending, its header names lowercased."""
        ...

    async def aclose(self) -> None:
        """Release underlying resources (connections, pools). Should be idempotent."""
        ...
