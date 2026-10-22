from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WsrMetrics(SdkBaseModel):
    """Performance metrics for the aggregated data.

    All metrics are based on last-touch attribution with a 14-day window."""

    clicks: Optional[int] = UNSET
    """Number of clicks on affiliate links. Defaults to 0 if no traffic data available."""

    orders: int = 0
    """Number of orders based on last-touch 14-day attribution. Defaults to 0 if no attribution data available."""

    gmv: float = 0.0
    """Gross Merchandise Value (GMV) in USD based on last-touch 14-day attribution. This represents the total revenue
    generated from orders attributed to affiliate links. Defaults to 0.0 if no attribution data available."""

    wsr_commission: float = Field(default=0.0, alias="wsrCommission")
    """Commission earned from Walmart Seller Referral (WSR) program in USD. This is the primary commission earned
    through the affiliate program. Defaults to 0.0 if no commission data available."""

    other_commission: float = Field(default=0.0, alias="otherCommission")
    """Commission earned from other promotional programs in USD. This includes any additional commissions beyond the WSR
    program. Defaults to 0.0 if no commission data available."""

    total_units: int = Field(default=0, alias="totalUnits")
    """Total number of units sold based on last-touch 14-day attribution. Defaults to 0 if no attribution data
    available."""


class WsrMetricsDict(TypedDict):
    clicks: NotRequired[int]
    orders: NotRequired[int]
    gmv: NotRequired[float]
    wsr_commission: NotRequired[float]
    other_commission: NotRequired[float]
    total_units: NotRequired[int]
