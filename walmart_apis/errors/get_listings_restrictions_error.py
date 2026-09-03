from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

GetListingsRestrictionsErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GetListingsRestrictionsError:
    def map(self, response: HttpResponse) -> GetListingsRestrictionsErrorBody:
        match response.status_code:
            case 400 | 403 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


get_listings_restrictions_error_mapper: Final[
    ErrorMapper[GetListingsRestrictionsErrorBody]
] = _GetListingsRestrictionsError()
