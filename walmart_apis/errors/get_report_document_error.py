from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

GetReportDocumentErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GetReportDocumentError:
    def map(self, response: HttpResponse) -> GetReportDocumentErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


get_report_document_error_mapper: Final[ErrorMapper[GetReportDocumentErrorBody]] = _GetReportDocumentError()
