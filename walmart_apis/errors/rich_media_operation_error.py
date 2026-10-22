from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

RichMediaOperationErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _RichMediaOperationError:
    def map(self, status_code: int, content: bytes) -> RichMediaOperationErrorBody:
        match status_code:
            case 400 | 401 | 403 | 429 | 500:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


rich_media_operation_error_mapper: Final[ErrorMapper[RichMediaOperationErrorBody]] = _RichMediaOperationError()
