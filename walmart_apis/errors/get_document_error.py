from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

GetDocumentErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GetDocumentError:
    def map(self, response: HttpResponse) -> GetDocumentErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


get_document_error_mapper: Final[ErrorMapper[GetDocumentErrorBody]] = _GetDocumentError()
