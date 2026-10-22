from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .header1 import Header1, Header1Dict
from .item_price_type import ItemPriceType, ItemPriceTypeDict


class PromotionalPriceResponse(SdkBaseModel):
    payload: Optional[ItemPriceType] = UNSET
    header: Optional[Header1] = UNSET
    status: Optional[str] = UNSET


class PromotionalPriceResponseDict(TypedDict):
    payload: NotRequired[ItemPriceTypeDict]
    header: NotRequired[Header1Dict]
    status: NotRequired[str]
