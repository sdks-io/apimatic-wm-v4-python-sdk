from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

ListAllFulfillmentOrdersErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _ListAllFulfillmentOrdersError:
    def map(self, response: HttpResponse) -> ListAllFulfillmentOrdersErrorBody:
        match response.status_code:
            case 400 | 403 | 429 | 500:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


list_all_fulfillment_orders_error_mapper: Final[
    ErrorMapper[ListAllFulfillmentOrdersErrorBody]
] = _ListAllFulfillmentOrdersError()
