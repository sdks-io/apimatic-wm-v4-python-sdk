from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CriteriaData(SdkBaseModel):
    """Shows the criteria for the Pro Seller badge."""

    orders: Optional[int] = UNSET
    """Number of orders received during the last 90 days."""

    delivery_defect_rate: Optional[str] = Field(default=UNSET, alias="deliveryDefectRate")
    """Delivery Defect rate in the given timeframe."""

    cancellation_rate: Optional[str] = Field(default=UNSET, alias="cancellationRate")
    """Cancellation rate in the given timeframe."""

    listing_quality_catalog: Optional[int] = Field(default=UNSET, alias="listingQualityCatalog")
    """Trending Catalog Quality Score coverage."""

    active_days: Optional[int] = Field(default=UNSET, alias="activeDays")
    """Days active on the platform."""


class CriteriaDataDict(TypedDict):
    orders: NotRequired[int]
    delivery_defect_rate: NotRequired[str]
    cancellation_rate: NotRequired[str]
    listing_quality_catalog: NotRequired[int]
    active_days: NotRequired[int]
