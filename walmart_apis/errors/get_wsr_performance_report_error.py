from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.wsr_error_response import WsrErrorResponse

GetWsrPerformanceReportErrorBody: TypeAlias = WsrErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _GetWsrPerformanceReportError:
    def map(self, status_code: int, content: bytes) -> GetWsrPerformanceReportErrorBody:
        match status_code:
            case 400 | 500:
                return decode_json[WsrErrorResponse](content)
            case _:
                return RawError(status_code, content)


get_wsr_performance_report_error_mapper: Final[
    ErrorMapper[GetWsrPerformanceReportErrorBody]
] = _GetWsrPerformanceReportError()
