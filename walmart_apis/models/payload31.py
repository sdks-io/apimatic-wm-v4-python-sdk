from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .recommended_item2 import RecommendedItem2, RecommendedItem2Dict
from .total_insight2 import TotalInsight2, TotalInsight2Dict


class Payload31(SdkBaseModel):
    recommended_items: Optional[list[RecommendedItem2]] = Field(default=UNSET, alias="recommendedItems")
    total_insights: Optional[list[TotalInsight2]] = Field(default=UNSET, alias="totalInsights")
    total_records: Optional[float] = Field(default=UNSET, alias="totalRecords")
    """Total number of WFS Unpublished insights available to you."""


class Payload31Dict(TypedDict):
    recommended_items: NotRequired[list[RecommendedItem2Dict]]
    total_insights: NotRequired[list[TotalInsight2Dict]]
    total_records: NotRequired[float]
