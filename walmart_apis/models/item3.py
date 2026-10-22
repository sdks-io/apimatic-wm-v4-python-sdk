from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .recommendation import Recommendation, RecommendationDict


class Item3(SdkBaseModel):
    item_id: Optional[str] = UNSET
    product_name: Optional[str] = UNSET
    short_description: Optional[str] = UNSET
    image_url: Optional[str] = UNSET
    sku: Optional[str] = UNSET
    walmart_url: Optional[str] = UNSET
    product_type: Optional[str] = UNSET
    status: Optional[str] = UNSET
    recommendation: Optional[Recommendation] = UNSET


class Item3Dict(TypedDict):
    item_id: NotRequired[str]
    product_name: NotRequired[str]
    short_description: NotRequired[str]
    image_url: NotRequired[str]
    sku: NotRequired[str]
    walmart_url: NotRequired[str]
    product_type: NotRequired[str]
    status: NotRequired[str]
    recommendation: NotRequired[RecommendationDict]
