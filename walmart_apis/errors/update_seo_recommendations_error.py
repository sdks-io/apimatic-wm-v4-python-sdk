from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_seo_recommendation_update_items400_error1 import V3SeoRecommendationUpdateItems400Error1
from ..models.v3_seo_recommendation_update_items404_error1 import V3SeoRecommendationUpdateItems404Error1
from ..models.v3_seo_recommendation_update_items500_error1 import V3SeoRecommendationUpdateItems500Error1

UpdateSeoRecommendationsErrorBody: TypeAlias = (
    V3SeoRecommendationUpdateItems400Error1
    | V3SeoRecommendationUpdateItems404Error1
    | V3SeoRecommendationUpdateItems500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _UpdateSeoRecommendationsError:
    def map(self, status_code: int, content: bytes) -> UpdateSeoRecommendationsErrorBody:
        match status_code:
            case 400:
                return decode_json[V3SeoRecommendationUpdateItems400Error1](content)
            case 404:
                return decode_json[V3SeoRecommendationUpdateItems404Error1](content)
            case 500:
                return decode_json[V3SeoRecommendationUpdateItems500Error1](content)
            case _:
                return RawError(status_code, content)


update_seo_recommendations_error_mapper: Final[
    ErrorMapper[UpdateSeoRecommendationsErrorBody]
] = _UpdateSeoRecommendationsError()
