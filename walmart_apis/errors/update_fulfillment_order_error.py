from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

UpdateFulfillmentOrderErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _UpdateFulfillmentOrderError:
    def map(self, response: HttpResponse) -> UpdateFulfillmentOrderErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


update_fulfillment_order_error_mapper: Final[
    ErrorMapper[UpdateFulfillmentOrderErrorBody]
] = _UpdateFulfillmentOrderError()
