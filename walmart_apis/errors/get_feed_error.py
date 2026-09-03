from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list1 import ErrorList1

GetFeedErrorBody: TypeAlias = ErrorList1 | RawError


@dataclass(frozen=True, slots=True)
class _GetFeedError:
    def map(self, response: HttpResponse) -> GetFeedErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList1](response)
            case _:
                return RawError(response)


get_feed_error_mapper: Final[ErrorMapper[GetFeedErrorBody]] = _GetFeedError()
