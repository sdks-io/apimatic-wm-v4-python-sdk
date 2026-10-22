from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.wsr_error_response import WsrErrorResponse

GetTagTemplatesErrorBody: TypeAlias = WsrErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _GetTagTemplatesError:
    def map(self, status_code: int, content: bytes) -> GetTagTemplatesErrorBody:
        match status_code:
            case 400 | 500:
                return decode_json[WsrErrorResponse](content)
            case _:
                return RawError(status_code, content)


get_tag_templates_error_mapper: Final[ErrorMapper[GetTagTemplatesErrorBody]] = _GetTagTemplatesError()
