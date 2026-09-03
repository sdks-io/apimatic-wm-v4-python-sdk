from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error3 import Error3

GetListingOffersErrorBody: TypeAlias = list[Error3] | RawError


@dataclass(frozen=True, slots=True)
class _GetListingOffersError:
    def map(self, response: HttpResponse) -> GetListingOffersErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[list[Error3]](response)
            case _:
                return RawError(response)


get_listing_offers_error_mapper: Final[ErrorMapper[GetListingOffersErrorBody]] = _GetListingOffersError()
