from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .mpitem import Mpitem, MpitemDict
from .mpitem_feed_header1 import MpitemFeedHeader1, MpitemFeedHeader1Dict


class V3PriceRequest(SdkBaseModel):
    mp_item_feed_header: Optional[MpitemFeedHeader1] = Field(default=UNSET, alias="MPItemFeedHeader")
    """<br><b style='color:green;'>Market availability: CA | MX | CL</b>"""

    mp_item: Optional[list[Mpitem]] = Field(default=UNSET, alias="MPItem")


class V3PriceRequestDict(TypedDict):
    mp_item_feed_header: NotRequired[MpitemFeedHeader1Dict]
    mp_item: NotRequired[list[MpitemDict]]
