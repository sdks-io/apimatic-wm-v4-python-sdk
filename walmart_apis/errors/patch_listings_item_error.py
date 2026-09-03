from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

PatchListingsItemErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _PatchListingsItemError:
    def map(self, response: HttpResponse) -> PatchListingsItemErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


patch_listings_item_error_mapper: Final[ErrorMapper[PatchListingsItemErrorBody]] = _PatchListingsItemError()
