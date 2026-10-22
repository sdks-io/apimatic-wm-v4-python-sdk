from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_response3 import ErrorResponse3
from ..models.error_responses import ErrorResponses
from ..models.forbidden1 import Forbidden1
from ..models.too_many_requests1 import TooManyRequests1
from ..models.unauthorized1 import Unauthorized1

ReturnOrderCursorErrorBody: TypeAlias = (
    ErrorResponse3 | Unauthorized1 | Forbidden1 | TooManyRequests1 | ErrorResponses | RawError
)


@dataclass(frozen=True, slots=True)
class _ReturnOrderCursorError:
    def map(self, status_code: int, content: bytes) -> ReturnOrderCursorErrorBody:
        match status_code:
            case 400:
                return decode_json[ErrorResponse3](content)
            case 401:
                return decode_json[Unauthorized1](content)
            case 403:
                return decode_json[Forbidden1](content)
            case 429:
                return decode_json[TooManyRequests1](content)
            case 500:
                return decode_json[ErrorResponses](content)
            case _:
                return RawError(status_code, content)


return_order_cursor_error_mapper: Final[ErrorMapper[ReturnOrderCursorErrorBody]] = _ReturnOrderCursorError()
