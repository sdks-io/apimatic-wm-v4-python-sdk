from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .mpitem_feed_header import MpitemFeedHeader, MpitemFeedHeaderDict
from .unions.mpitem11 import Mpitem11, Mpitem11Dict


class V3FeedsFeedTypePriceAndPromotionRequest(SdkBaseModel):
    mp_item_feed_header: Optional[MpitemFeedHeader] = Field(default=UNSET, alias="MPItemFeedHeader")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    mp_item: Optional[Mpitem11] = Field(default=UNSET, alias="MPItem")


class V3FeedsFeedTypePriceAndPromotionRequestDict(TypedDict):
    mp_item_feed_header: NotRequired[MpitemFeedHeaderDict]
    mp_item: NotRequired[Mpitem11Dict]
