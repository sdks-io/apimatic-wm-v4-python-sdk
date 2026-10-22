from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .recommended_item1 import RecommendedItem1, RecommendedItem1Dict
from .total_insight1 import TotalInsight1, TotalInsight1Dict


class Payload22(SdkBaseModel):
    recommended_items: Optional[list[RecommendedItem1]] = Field(default=UNSET, alias="recommendedItems")
    total_insights: Optional[list[TotalInsight1]] = Field(default=UNSET, alias="totalInsights")
    total_records: Optional[float] = Field(default=UNSET, alias="totalRecords")
    """Total number of Fulfill with WFS insights available to you."""


class Payload22Dict(TypedDict):
    recommended_items: NotRequired[list[RecommendedItem1Dict]]
    total_insights: NotRequired[list[TotalInsight1Dict]]
    total_records: NotRequired[float]
