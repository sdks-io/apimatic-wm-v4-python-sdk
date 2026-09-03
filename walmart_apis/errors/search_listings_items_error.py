from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

SearchListingsItemsErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _SearchListingsItemsError:
    def map(self, response: HttpResponse) -> SearchListingsItemsErrorBody:
        match response.status_code:
            case 400 | 403 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


search_listings_items_error_mapper: Final[ErrorMapper[SearchListingsItemsErrorBody]] = _SearchListingsItemsError()
