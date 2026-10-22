from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Recommendations(SdkBaseModel):
    """Recommendations on how to increase chances of Pro Seller Badge eligibility"""

    delivery_defect_rate: Optional[str] = Field(default=UNSET, alias="deliveryDefectRate")
    """Recommendations on reducing the delivery defect rate"""

    cancellation_rate: Optional[str] = Field(default=UNSET, alias="cancellationRate")
    """Recommendations on reducing the Cancellation rate"""

    listing_quality_catalog: Optional[str] = Field(default=UNSET, alias="listingQualityCatalog")
    """Recommendations on increasing the trending item catalog coverage"""


class RecommendationsDict(TypedDict):
    delivery_defect_rate: NotRequired[str]
    cancellation_rate: NotRequired[str]
    listing_quality_catalog: NotRequired[str]
