from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_insights_items_listing_quality_count400_error1 import V3InsightsItemsListingQualityCount400Error1
from ..models.v3_insights_items_listing_quality_count500_error1 import V3InsightsItemsListingQualityCount500Error1
from ..models.v3_token400_error1 import V3Token400Error1

GetCategoriesListErrorBody: TypeAlias = (
    V3InsightsItemsListingQualityCount400Error1
    | V3Token400Error1
    | V3InsightsItemsListingQualityCount500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _GetCategoriesListError:
    def map(self, status_code: int, content: bytes) -> GetCategoriesListErrorBody:
        match status_code:
            case 400:
                return decode_json[V3InsightsItemsListingQualityCount400Error1](content)
            case 401 | 403:
                return decode_json[V3Token400Error1](content)
            case 500:
                return decode_json[V3InsightsItemsListingQualityCount500Error1](content)
            case _:
                return RawError(status_code, content)


get_categories_list_error_mapper: Final[ErrorMapper[GetCategoriesListErrorBody]] = _GetCategoriesListError()
