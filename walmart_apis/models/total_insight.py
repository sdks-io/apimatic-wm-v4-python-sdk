from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TotalInsight(SdkBaseModel):
    total_estimated_sales_lift: Optional[float] = Field(default=UNSET, alias="totalEstimatedSalesLift")
    """Estimated total dollar amount you could lose in sales each day if both out-of-stock and at-risk items are not
    restocked."""

    total_forecasted_sales_lost: Optional[float] = Field(default=UNSET, alias="totalForecastedSalesLost")
    """Estimated dollar amount you could lose in sales each day if all out-of-stock items are not restocked."""

    total_forecasted_sales_at_risk: Optional[float] = Field(default=UNSET, alias="totalForecastedSalesAtRisk")
    """Estimated dollar amount you could lose in daily sales if all items with under 4 weeks of supply are not
    restocked."""


class TotalInsightDict(TypedDict):
    total_estimated_sales_lift: NotRequired[float]
    total_forecasted_sales_lost: NotRequired[float]
    total_forecasted_sales_at_risk: NotRequired[float]
