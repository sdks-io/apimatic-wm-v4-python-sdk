from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

DownloadOldReportErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _DownloadOldReportError:
    def map(self, response: HttpResponse) -> DownloadOldReportErrorBody:
        match response.status_code:
            case 400 | 404 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


download_old_report_error_mapper: Final[ErrorMapper[DownloadOldReportErrorBody]] = _DownloadOldReportError()
