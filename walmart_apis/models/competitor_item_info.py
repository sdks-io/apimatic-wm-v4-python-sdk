from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .price1 import Price1, Price1Dict


class CompetitorItemInfo(SdkBaseModel):
    """Competitor's item information"""

    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    """Competitor item id."""

    url: Optional[str] = UNSET
    """Competitor item url."""

    item_price: Optional[Price1] = Field(default=UNSET, alias="itemPrice")
    """Competitor's item shipping price details of the item recommendation."""

    shipping_price: Optional[Price1] = Field(default=UNSET, alias="shippingPrice")
    """Competitor's item shipping price details of the item recommendation."""


class CompetitorItemInfoDict(TypedDict):
    item_id: NotRequired[str]
    url: NotRequired[str]
    item_price: NotRequired[Price1Dict]
    shipping_price: NotRequired[Price1Dict]
