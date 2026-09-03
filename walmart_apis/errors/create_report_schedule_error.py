from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

CreateReportScheduleErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _CreateReportScheduleError:
    def map(self, response: HttpResponse) -> CreateReportScheduleErrorBody:
        match response.status_code:
            case 400 | 403 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


create_report_schedule_error_mapper: Final[ErrorMapper[CreateReportScheduleErrorBody]] = _CreateReportScheduleError()
