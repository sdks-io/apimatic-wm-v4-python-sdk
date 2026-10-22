from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .mpitem_feed_header import MpitemFeedHeader, MpitemFeedHeaderDict
from .unions.mpitem111 import Mpitem111, Mpitem111Dict


class V3FeedsFeedTypePriceAndPromotionRequest1(SdkBaseModel):
    mp_item_feed_header: Optional[MpitemFeedHeader] = Field(default=UNSET, alias="MPItemFeedHeader")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    mp_item: Optional[Mpitem111] = Field(default=UNSET, alias="MPItem")


class V3FeedsFeedTypePriceAndPromotionRequest1Dict(TypedDict):
    mp_item_feed_header: NotRequired[MpitemFeedHeaderDict]
    mp_item: NotRequired[Mpitem111Dict]
