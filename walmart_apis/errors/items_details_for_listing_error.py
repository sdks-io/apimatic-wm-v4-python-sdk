from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_insights_items_listing_quality_items500_error1 import V3InsightsItemsListingQualityItems500Error1
from ..models.v3_token400_error1 import V3Token400Error1

ItemsDetailsForListingErrorBody: TypeAlias = V3Token400Error1 | V3InsightsItemsListingQualityItems500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _ItemsDetailsForListingError:
    def map(self, status_code: int, content: bytes) -> ItemsDetailsForListingErrorBody:
        match status_code:
            case 401 | 403:
                return decode_json[V3Token400Error1](content)
            case 500:
                return decode_json[V3InsightsItemsListingQualityItems500Error1](content)
            case _:
                return RawError(status_code, content)


items_details_for_listing_error_mapper: Final[
    ErrorMapper[ItemsDetailsForListingErrorBody]
] = _ItemsDetailsForListingError()
