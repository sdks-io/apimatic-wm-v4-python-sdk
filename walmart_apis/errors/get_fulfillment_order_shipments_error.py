from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

GetFulfillmentOrderShipmentsErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GetFulfillmentOrderShipmentsError:
    def map(self, response: HttpResponse) -> GetFulfillmentOrderShipmentsErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


get_fulfillment_order_shipments_error_mapper: Final[
    ErrorMapper[GetFulfillmentOrderShipmentsErrorBody]
] = _GetFulfillmentOrderShipmentsError()
