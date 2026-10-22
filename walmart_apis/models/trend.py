from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .trend_datum import TrendDatum, TrendDatumDict


class Trend(SdkBaseModel):
    trend_type: Optional[str] = Field(default=UNSET, alias="trendType")
    """Type of trend.

     Values: DEMAND_TRENDS, PRICE_TRENDS"""

    trend_data: Optional[list[TrendDatum]] = Field(default=UNSET, alias="trendData")
    """Trend data for the recommended item. The array will be empty if trends are not available for the item."""


class TrendDict(TypedDict):
    trend_type: NotRequired[str]
    trend_data: NotRequired[list[TrendDatumDict]]
