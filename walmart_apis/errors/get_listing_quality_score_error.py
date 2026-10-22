from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_insights_items_listing_quality_score400_error1 import V3InsightsItemsListingQualityScore400Error1
from ..models.v3_insights_items_listing_quality_score500_error1 import V3InsightsItemsListingQualityScore500Error1
from ..models.v3_token400_error1 import V3Token400Error1

GetListingQualityScoreErrorBody: TypeAlias = (
    V3InsightsItemsListingQualityScore400Error1
    | V3Token400Error1
    | V3InsightsItemsListingQualityScore500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _GetListingQualityScoreError:
    def map(self, status_code: int, content: bytes) -> GetListingQualityScoreErrorBody:
        match status_code:
            case 400:
                return decode_json[V3InsightsItemsListingQualityScore400Error1](content)
            case 401 | 403:
                return decode_json[V3Token400Error1](content)
            case 500:
                return decode_json[V3InsightsItemsListingQualityScore500Error1](content)
            case _:
                return RawError(status_code, content)


get_listing_quality_score_error_mapper: Final[
    ErrorMapper[GetListingQualityScoreErrorBody]
] = _GetListingQualityScoreError()
