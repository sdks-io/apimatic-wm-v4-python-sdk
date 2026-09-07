"""Reading a response's ``Content-Disposition``: the filename it suggests, made safe to use.

Response-side parsing lives beside the request-side header module but not inside it:
``headers.py`` renders and resolves *outbound* layers, and this module never touches a request.

The standard library gets this header wrong twice, both reproduced during planning
(docs/plans/file-handling.md, verified facts). ``Message.get_filename()`` returns the plain
``filename`` when both forms are present -- RFC 6266 §4.3 requires the extended ``filename*`` to
win -- and the RFC 2231 machinery percent-decodes the extended value as latin-1 whatever charset
it declares, so the text must be re-encoded through latin-1 and decoded with the declared charset
to come back intact.

Both functions treat their input as attacker-controlled. The parser is **total**: any malformed
header yields ``None`` rather than raising, because it runs while a streamed connection is held
and a raise there would leak it. The sanitiser is the paranoid half: a server-suggested name is
reduced to a basename, stripped of everything Windows refuses, and refused outright when what
survives is empty, a reserved device name, or too long to create."""

from __future__ import annotations

import re
from email.message import Message
from typing import Final

_SEPARATORS: Final = re.compile(r"[\\/]")
_WINDOWS_ILLEGAL: Final = frozenset('<>:"|?*')
_WINDOWS_RESERVED: Final = frozenset(
    {"CON", "PRN", "AUX", "NUL"} | {f"COM{d}" for d in "123456789"} | {f"LPT{d}" for d in "123456789"}
)


def content_disposition_filename(header: str | None) -> str | None:
    """The filename a ``Content-Disposition`` suggests, or ``None``.

    Prefers the RFC 8187 extended ``filename*`` (RFC 6266 §4.3) and recovers its text from the
    standard library's latin-1 percent-decode; RFC 8187 §3.2.1 permits only UTF-8, so any other
    declared charset falls back to the plain ``filename`` rather than guessing. Continuation
    segments (``filename*0*``, ``filename*1*``) are collapsed by the same machinery.

    Total by design: a malformed header returns ``None``, never raises -- this runs between a
    streamed response's head arriving and its owner returning, where a raise would leak the
    connection. The result is *not* trusted as a path; see :func:`safe_filename`.

    Args:
        header: The header's value, or ``None`` when the response carried none.

    Returns:
        The suggested filename, or ``None`` when there is no usable one."""
    if header is None:
        return None
    try:
        message = Message()
        message["content-disposition"] = header
        params = message.get_params(header="content-disposition")
        if params is None:
            return None

        plain: str | None = None
        extended: str | None = None
        for name, raw in params:
            if name != "filename":
                continue
            # The parser hands back a plain parameter as ``str`` and an RFC 2231 extended one as a
            # ``(charset, language, text)`` tuple. A duplicated plain form keeps its first
            # occurrence; duplicated extended forms never reach here -- the stdlib merges them as
            # continuations before ``get_params`` returns.
            value: object = raw
            if isinstance(value, str) and plain is None:
                plain = value
            elif isinstance(value, tuple) and extended is None:
                extended = _decode_extended(value)
        return (extended or plain) or None
    except Exception:
        # Total by design -- the docstring says why. Bad wire data degrades, never raises.
        return None


def _decode_extended(value: tuple[object, ...]) -> str | None:
    # (charset, language, text) -- text percent-decoded as latin-1 by the parser regardless of the
    # declared charset, which is the mojibake the round trip below undoes.
    if len(value) != 3:
        return None
    charset, _language, text = value
    if not isinstance(charset, str) or not isinstance(text, str):
        return None
    if charset.lower() not in ("utf-8", "utf8"):
        return None
    try:
        return text.encode("latin-1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return None


def safe_filename(filename: str) -> str:
    """Reduce a server-supplied filename to a name safe to create in a directory.

    Basename first, under both separator flavours -- ``Content-Disposition`` is
    attacker-controlled and ``filename="../../etc/passwd"`` reaches the parser unchanged -- then
    strip what Windows refuses: ``<>:"|?*``, unprintable characters, and trailing dots or spaces.
    Dropping the colon also neutralises an NTFS alternate-data-stream name. What remains is
    refused rather than mangled when it cannot safely name a file: a reserved device-name stem
    (``CON``, ``NUL``, ``COM1``... -- Windows 10 resolves even ``CON.pdf`` to the console device,
    and a bare ``NUL`` open "succeeds" while the bytes go to the null device) or a name past 255
    characters, the per-component ceiling on NTFS and most POSIX filesystems.

    Args:
        filename: The server's suggestion, as :func:`content_disposition_filename` returned it.

    Returns:
        The reduced name, never empty.

    Raises:
        ValueError: If nothing safe remains -- an empty reduction, ``.`` or ``..``, a reserved
            device name, or a name too long to create."""
    basename = _SEPARATORS.split(filename)[-1]
    cleaned = "".join(ch for ch in basename if ch not in _WINDOWS_ILLEGAL and ch.isprintable())
    cleaned = cleaned.rstrip(". ")
    # A reserved stem is matched as Windows does: up to the first dot, trailing spaces ignored.
    stem = cleaned.split(".", 1)[0].rstrip(" ")
    if not cleaned or stem.upper() in _WINDOWS_RESERVED or len(cleaned) > 255:
        raise ValueError(f"{filename!r} reduces to nothing safe to create -- pass an explicit file path instead")
    return cleaned
