from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WeeklyTrend(SdkBaseModel):
    week: Optional[str] = UNSET
    """Week of the year. Example: 24"""

    year: Optional[str] = UNSET
    """Year of trend. Example: 2024"""

    value: Optional[float] = UNSET
    """| Trend Type | Description | Data type of value |
    | --- | ----------- | ------- |
    | PRICE_TRENDS | Indicates the price of the item in the market specific currency for the given week and year.
        Example: 6.54 | double |
    | DEMAND_TRENDS | Normalised values to indicate relative demand for the recommendation for the given week. Example:
        0.08 | double |"""


class WeeklyTrendDict(TypedDict):
    week: NotRequired[str]
    year: NotRequired[str]
    value: NotRequired[float]
