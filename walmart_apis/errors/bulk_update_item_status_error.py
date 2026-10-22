from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_growth_reviews_accelerator_items_status400_error1 import V3GrowthReviewsAcceleratorItemsStatus400Error1
from ..models.v3_growth_reviews_accelerator_items_status401_error1 import V3GrowthReviewsAcceleratorItemsStatus401Error1
from ..models.v3_growth_reviews_accelerator_items_status403_error1 import V3GrowthReviewsAcceleratorItemsStatus403Error1
from ..models.v3_growth_reviews_accelerator_items_status500_error1 import V3GrowthReviewsAcceleratorItemsStatus500Error1

BulkUpdateItemStatusErrorBody: TypeAlias = (
    V3GrowthReviewsAcceleratorItemsStatus400Error1
    | V3GrowthReviewsAcceleratorItemsStatus401Error1
    | V3GrowthReviewsAcceleratorItemsStatus403Error1
    | V3GrowthReviewsAcceleratorItemsStatus500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _BulkUpdateItemStatusError:
    def map(self, status_code: int, content: bytes) -> BulkUpdateItemStatusErrorBody:
        match status_code:
            case 400:
                return decode_json[V3GrowthReviewsAcceleratorItemsStatus400Error1](content)
            case 401:
                return decode_json[V3GrowthReviewsAcceleratorItemsStatus401Error1](content)
            case 403:
                return decode_json[V3GrowthReviewsAcceleratorItemsStatus403Error1](content)
            case 500:
                return decode_json[V3GrowthReviewsAcceleratorItemsStatus500Error1](content)
            case _:
                return RawError(status_code, content)


bulk_update_item_status_error_mapper: Final[ErrorMapper[BulkUpdateItemStatusErrorBody]] = _BulkUpdateItemStatusError()
