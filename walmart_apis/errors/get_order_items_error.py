from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list import ErrorList

GetOrderItemsErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GetOrderItemsError:
    def map(self, response: HttpResponse) -> GetOrderItemsErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429 | 500 | 503:
                return decode_json[ErrorList](response)
            case _:
                return RawError(response)


get_order_items_error_mapper: Final[ErrorMapper[GetOrderItemsErrorBody]] = _GetOrderItemsError()
