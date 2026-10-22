from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .recommended_item import RecommendedItem, RecommendedItemDict
from .total_insight import TotalInsight, TotalInsightDict


class Payload110(SdkBaseModel):
    recommended_items: Optional[list[RecommendedItem]] = Field(default=UNSET, alias="recommendedItems")
    total_insights: Optional[list[TotalInsight]] = Field(default=UNSET, alias="totalInsights")
    total_records: Optional[float] = Field(default=UNSET, alias="totalRecords")
    """The total number of item-level restock insights available to you."""


class Payload110Dict(TypedDict):
    recommended_items: NotRequired[list[RecommendedItemDict]]
    total_insights: NotRequired[list[TotalInsightDict]]
    total_records: NotRequired[float]
