from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_response2 import ErrorResponse2
from ..models.not_found_response import NotFoundResponse

GetShipmentQuantityRecommendationsErrorBody: TypeAlias = ErrorResponse2 | NotFoundResponse | RawError


@dataclass(frozen=True, slots=True)
class _GetShipmentQuantityRecommendationsError:
    def map(self, status_code: int, content: bytes) -> GetShipmentQuantityRecommendationsErrorBody:
        match status_code:
            case 400 | 500:
                return decode_json[ErrorResponse2](content)
            case 404:
                return decode_json[NotFoundResponse](content)
            case _:
                return RawError(status_code, content)


get_shipment_quantity_recommendations_error_mapper: Final[
    ErrorMapper[GetShipmentQuantityRecommendationsErrorBody]
] = _GetShipmentQuantityRecommendationsError()
