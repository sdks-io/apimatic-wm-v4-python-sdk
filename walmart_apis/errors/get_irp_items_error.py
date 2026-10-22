from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_growth_reviews_accelerator_items400_error1 import V3GrowthReviewsAcceleratorItems400Error1
from ..models.v3_growth_reviews_accelerator_items401_error1 import V3GrowthReviewsAcceleratorItems401Error1
from ..models.v3_growth_reviews_accelerator_items403_error1 import V3GrowthReviewsAcceleratorItems403Error1
from ..models.v3_insights_items_listing_quality_items500_error1 import V3InsightsItemsListingQualityItems500Error1

GetIrpItemsErrorBody: TypeAlias = (
    V3GrowthReviewsAcceleratorItems400Error1
    | V3GrowthReviewsAcceleratorItems401Error1
    | V3GrowthReviewsAcceleratorItems403Error1
    | V3InsightsItemsListingQualityItems500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _GetIrpItemsError:
    def map(self, status_code: int, content: bytes) -> GetIrpItemsErrorBody:
        match status_code:
            case 400:
                return decode_json[V3GrowthReviewsAcceleratorItems400Error1](content)
            case 401:
                return decode_json[V3GrowthReviewsAcceleratorItems401Error1](content)
            case 403:
                return decode_json[V3GrowthReviewsAcceleratorItems403Error1](content)
            case 500:
                return decode_json[V3InsightsItemsListingQualityItems500Error1](content)
            case _:
                return RawError(status_code, content)


get_irp_items_error_mapper: Final[ErrorMapper[GetIrpItemsErrorBody]] = _GetIrpItemsError()
