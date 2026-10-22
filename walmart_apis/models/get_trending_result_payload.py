from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .trending_item import TrendingItem, TrendingItemDict


class GetTrendingResultPayload(SdkBaseModel):
    total_count: Optional[int] = Field(default=UNSET, alias="totalCount")
    """Total count of qualified items"""

    items: Optional[list[TrendingItem]] = UNSET
    """List of Qualified Items"""


class GetTrendingResultPayloadDict(TypedDict):
    total_count: NotRequired[int]
    items: NotRequired[list[TrendingItemDict]]
