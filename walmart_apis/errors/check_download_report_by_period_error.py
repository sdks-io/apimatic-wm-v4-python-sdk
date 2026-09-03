from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

CheckDownloadReportByPeriodErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _CheckDownloadReportByPeriodError:
    def map(self, response: HttpResponse) -> CheckDownloadReportByPeriodErrorBody:
        match response.status_code:
            case 400 | 401 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


check_download_report_by_period_error_mapper: Final[
    ErrorMapper[CheckDownloadReportByPeriodErrorBody]
] = _CheckDownloadReportByPeriodError()
