from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TotalInsight1(SdkBaseModel):
    seller_fulfilled_past30_days_sales: Optional[float] = Field(default=UNSET, alias="sellerFulfilledPast30DaysSales")
    """What you currently earn from seller-fulfilled items, based on your weekly average sales from the past 30 days."""

    walmart_fulfilled_estimated_sales: Optional[float] = Field(default=UNSET, alias="walmartFulfilledEstimatedSales")
    """What we predict you’ll earn if you convert the following items to WFS and send the suggested quantities. This is
    the sum of your predicted WFS GMV in the 30 days after your items are available to sell. To leverage these
    suggestions, we recommend you convert and send your items to WFS within the next 4 weeks."""

    total_estimated_sales_lift: Optional[float] = Field(default=UNSET, alias="totalEstimatedSalesLift")
    """Total estimated sales lift if these items are converted to WFS and sold within the next 30 days of recommendation
    generation. This is your Walmart-fulfilled GMV minus seller-fulfilled GMV."""


class TotalInsight1Dict(TypedDict):
    seller_fulfilled_past30_days_sales: NotRequired[float]
    walmart_fulfilled_estimated_sales: NotRequired[float]
    total_estimated_sales_lift: NotRequired[float]
