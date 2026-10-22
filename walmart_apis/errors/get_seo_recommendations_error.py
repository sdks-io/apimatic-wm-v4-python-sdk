from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_seo_recommendation_get_items400_error1 import V3SeoRecommendationGetItems400Error1
from ..models.v3_seo_recommendation_get_items500_error1 import V3SeoRecommendationGetItems500Error1

GetSeoRecommendationsErrorBody: TypeAlias = (
    V3SeoRecommendationGetItems400Error1 | V3SeoRecommendationGetItems500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _GetSeoRecommendationsError:
    def map(self, status_code: int, content: bytes) -> GetSeoRecommendationsErrorBody:
        match status_code:
            case 400:
                return decode_json[V3SeoRecommendationGetItems400Error1](content)
            case 500:
                return decode_json[V3SeoRecommendationGetItems500Error1](content)
            case _:
                return RawError(status_code, content)


get_seo_recommendations_error_mapper: Final[ErrorMapper[GetSeoRecommendationsErrorBody]] = _GetSeoRecommendationsError()
