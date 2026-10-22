from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_response1 import ErrorResponse1
from ..models.v3_token500_error1 import V3Token500Error1

GetCategorizationDetailsOfAssortmentRecommendationsErrorBody: TypeAlias = ErrorResponse1 | V3Token500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _GetCategorizationDetailsOfAssortmentRecommendationsError:
    def map(self, status_code: int, content: bytes) -> GetCategorizationDetailsOfAssortmentRecommendationsErrorBody:
        match status_code:
            case 400 | 500:
                return decode_json[ErrorResponse1](content)
            case 403:
                return decode_json[V3Token500Error1](content)
            case _:
                return RawError(status_code, content)


get_categorization_details_of_assortment_recommendations_error_mapper: Final[
    ErrorMapper[GetCategorizationDetailsOfAssortmentRecommendationsErrorBody]
] = _GetCategorizationDetailsOfAssortmentRecommendationsError()
