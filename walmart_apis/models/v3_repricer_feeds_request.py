from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item11 import Item11, Item11Dict
from .item_feed_header import ItemFeedHeader, ItemFeedHeaderDict


class V3RepricerFeedsRequest(SdkBaseModel):
    item_feed_header: Optional[ItemFeedHeader] = Field(default=UNSET, alias="ItemFeedHeader")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    item: Optional[list[Item11]] = Field(default=UNSET, alias="Item")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class V3RepricerFeedsRequestDict(TypedDict):
    item_feed_header: NotRequired[ItemFeedHeaderDict]
    item: NotRequired[list[Item11Dict]]
