from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

OneClickShipmentErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _OneClickShipmentError:
    def map(self, response: HttpResponse) -> OneClickShipmentErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


one_click_shipment_error_mapper: Final[ErrorMapper[OneClickShipmentErrorBody]] = _OneClickShipmentError()
