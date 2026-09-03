from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

GetShipment2ErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GetShipment2Error:
    def map(self, response: HttpResponse) -> GetShipment2ErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


get_shipment2_error_mapper: Final[ErrorMapper[GetShipment2ErrorBody]] = _GetShipment2Error()
