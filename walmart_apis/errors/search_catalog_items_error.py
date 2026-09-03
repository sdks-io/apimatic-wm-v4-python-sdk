from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

SearchCatalogItemsErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _SearchCatalogItemsError:
    def map(self, response: HttpResponse) -> SearchCatalogItemsErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


search_catalog_items_error_mapper: Final[ErrorMapper[SearchCatalogItemsErrorBody]] = _SearchCatalogItemsError()
