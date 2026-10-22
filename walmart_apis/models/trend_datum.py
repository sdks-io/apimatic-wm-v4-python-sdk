from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta9 import Meta9, Meta9Dict
from .monthly_trend import MonthlyTrend, MonthlyTrendDict
from .weekly_trend import WeeklyTrend, WeeklyTrendDict


class TrendDatum(SdkBaseModel):
    meta: Optional[Meta9] = UNSET
    """Meta information related to the trends response."""

    monthly_trends: Optional[list[MonthlyTrend]] = Field(default=UNSET, alias="monthlyTrends")
    """Trend data at a monthly level."""

    weekly_trends: Optional[list[WeeklyTrend]] = Field(default=UNSET, alias="weeklyTrends")
    """Trend data at a weekly level.<br><b style='color:green;'>Market availability: US only</span></b>"""


class TrendDatumDict(TypedDict):
    meta: NotRequired[Meta9Dict]
    monthly_trends: NotRequired[list[MonthlyTrendDict]]
    weekly_trends: NotRequired[list[WeeklyTrendDict]]
