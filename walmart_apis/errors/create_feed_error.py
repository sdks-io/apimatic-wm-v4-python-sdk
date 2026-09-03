from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list1 import ErrorList1

CreateFeedErrorBody: TypeAlias = ErrorList1 | RawError


@dataclass(frozen=True, slots=True)
class _CreateFeedError:
    def map(self, response: HttpResponse) -> CreateFeedErrorBody:
        match response.status_code:
            case 400 | 403 | 429 | 500:
                return decode_json[ErrorList1](response)
            case _:
                return RawError(response)


create_feed_error_mapper: Final[ErrorMapper[CreateFeedErrorBody]] = _CreateFeedError()
