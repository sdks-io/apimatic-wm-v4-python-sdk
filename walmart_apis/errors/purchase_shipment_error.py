from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

PurchaseShipmentErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _PurchaseShipmentError:
    def map(self, response: HttpResponse) -> PurchaseShipmentErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


purchase_shipment_error_mapper: Final[ErrorMapper[PurchaseShipmentErrorBody]] = _PurchaseShipmentError()
