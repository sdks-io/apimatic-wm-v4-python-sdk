from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MonthlyTrend(SdkBaseModel):
    month: Optional[str] = UNSET
    """Month of the year.

     Values: JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC"""

    year: Optional[str] = UNSET
    """Year of trend.

     Example: 2024"""

    value: Optional[float] = UNSET
    """| Trend Type | Description | Data type of value |
    | --- | ----------- | ------- |
    | PRICE_TRENDS | Indicates the price of the item in the market specific currency for the given month and year.
        Example: 5.99 | double |
    | DEMAND_TRENDS | Normalised values to indicate relative demand for the recommendation for the given month. Example:
        0.07 | double |"""


class MonthlyTrendDict(TypedDict):
    month: NotRequired[str]
    year: NotRequired[str]
    value: NotRequired[float]
