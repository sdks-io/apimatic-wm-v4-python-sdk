from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

DownloadReconciliationReportErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _DownloadReconciliationReportError:
    def map(self, response: HttpResponse) -> DownloadReconciliationReportErrorBody:
        match response.status_code:
            case 400 | 401 | 404 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


download_reconciliation_report_error_mapper: Final[
    ErrorMapper[DownloadReconciliationReportErrorBody]
] = _DownloadReconciliationReportError()
