from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_token500_error1 import V3Token500Error1

PriceBulkUploadsErrorBody: TypeAlias = V3Token500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _PriceBulkUploadsError:
    def map(self, status_code: int, content: bytes) -> PriceBulkUploadsErrorBody:
        match status_code:
            case 401 | 500:
                return decode_json[V3Token500Error1](content)
            case _:
                return RawError(status_code, content)


price_bulk_uploads_error_mapper: Final[ErrorMapper[PriceBulkUploadsErrorBody]] = _PriceBulkUploadsError()
