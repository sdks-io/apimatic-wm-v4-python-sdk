from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

DownloadNewReportErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _DownloadNewReportError:
    def map(self, response: HttpResponse) -> DownloadNewReportErrorBody:
        match response.status_code:
            case 400 | 404 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


download_new_report_error_mapper: Final[ErrorMapper[DownloadNewReportErrorBody]] = _DownloadNewReportError()
