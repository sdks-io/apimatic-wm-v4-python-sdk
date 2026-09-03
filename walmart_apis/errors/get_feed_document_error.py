from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list1 import ErrorList1

GetFeedDocumentErrorBody: TypeAlias = ErrorList1 | RawError


@dataclass(frozen=True, slots=True)
class _GetFeedDocumentError:
    def map(self, response: HttpResponse) -> GetFeedDocumentErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList1](response)
            case _:
                return RawError(response)


get_feed_document_error_mapper: Final[ErrorMapper[GetFeedDocumentErrorBody]] = _GetFeedDocumentError()
