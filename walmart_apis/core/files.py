"""What a caller may hand an endpoint as file content, and how a part describes itself.

A file never reaches the model layer. It is not validated by pydantic, not dumped through an
adapter, and not carried on ``SdkBaseModel`` -- which is why a file parameter names no declared
type in a subscript where every other parameter does: there is no adapter for it to name.

**Memory and ownership.** Every spelling below streams except ``bytes``, which the caller already
holds. A ``Path`` is opened by the transport on the send's ``ExitStack`` and read in 64 KiB chunks,
so the safest spelling is also the shortest one -- and the handle the transport opened is closed
when the send returns or raises, never later and never by a finalizer. A handle *you* open stays
yours: the SDK never closes a caller-supplied reader.

**Position.** A multipart part rewinds a seekable handle to 0 before reading it; a raw body reads
from wherever it sits. That is the underlying library's rule, and it is stated here because it
decides what happens to a handle you hand in mid-file.

**The async multipart caveat, stated where it bites.** httpx encodes a multipart body from a
synchronous chunk generator in both flavours (``MultipartStream.__aiter__`` yields from
``iter_chunks``), so on the async client each 64 KiB read is a blocking syscall on the loop thread.
A raw binary body does not share this: every sync arm is adapted to an async stream reading through
``asyncio.to_thread``, and the two async arms are consumed natively. Passing ``bytes`` avoids it
entirely at the cost of residency."""

from __future__ import annotations

from collections.abc import AsyncIterable, Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol, TypeAlias, runtime_checkable


@runtime_checkable
class BinaryReader(Protocol):
    """Anything with a binary ``read`` -- a file object, a ``SpooledTemporaryFile``, a ``GzipFile``.

    Structural rather than a list of concrete classes, which is what lets every custom reader work
    without being enumerated."""

    def read(self, size: int = -1, /) -> bytes: ...


@runtime_checkable
class AsyncBinaryReader(Protocol):
    """Anything with an awaitable binary ``read`` -- ``anyio.AsyncFile`` and kin.

    Note for the transport, stated once here: ``isinstance`` cannot tell this protocol from
    :class:`BinaryReader` -- ``runtime_checkable`` checks only that ``read`` exists -- so runtime
    dispatch goes through a ``TypeIs`` guard on ``iscoroutinefunction``, never a class pattern."""

    async def read(self, size: int = -1, /) -> bytes: ...


FileContent: TypeAlias = bytes | bytearray | Path | BinaryReader
"""What may be a multipart part's content.

Deliberately no ``str`` arm: a bare string is unresolvably either a path or the content itself, and
the library this rides on reads it as the content."""


@dataclass(frozen=True, slots=True)
class NamedFile:
    """File content plus the two things a caller may want to override about its part.

    Pass bare content when the defaults are right -- the filename comes from a ``Path`` or from a
    handle's own ``name``, and the media type from the operation's declared one. Name this only to
    override either.

    Two, and deliberately not three: RFC 7578 §4.8 allows a form-data part only ``Content-Type``,
    ``Content-Disposition`` and a deprecated ``Content-Transfer-Encoding``, and both live ones are
    owned already -- the media type by this class, the disposition by the resolved filename. A
    ``headers`` field could carry only fields a conforming receiver must ignore."""

    content: FileContent
    filename: str | None = None
    media_type: str | None = None


FileInput: TypeAlias = FileContent | NamedFile
"""What a file parameter accepts: content, or content with its part overridden."""

BinaryInput: TypeAlias = FileContent | Iterable[bytes]
"""What a raw binary body accepts on the sync client.

No ``NamedFile`` arm: a raw body has no part whose filename or media type could be overridden, so
accepting one would silently ignore both. The iterable arm is the progress hook: a generator that
yields chunks may count them on the way past."""

AsyncBinaryInput: TypeAlias = BinaryInput | AsyncBinaryReader | AsyncIterable[bytes]
"""The async client's raw binary body.

Every sync arm is adapted to an async stream that reads through ``asyncio.to_thread``, so the leg
streams *and* leaves the loop free; the two async arms are consumed natively on the loop."""
