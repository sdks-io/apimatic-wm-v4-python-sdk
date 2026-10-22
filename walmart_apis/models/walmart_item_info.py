from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .price1 import Price1, Price1Dict


class WalmartItemInfo(SdkBaseModel):
    """Walmart's item information"""

    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    """Walmart item ID."""

    url: Optional[str] = UNSET
    """Walmart item URL."""

    wfs_indicator: Optional[bool] = Field(default=UNSET, alias="wfsIndicator")
    """Walmart fulfilment service indicator."""

    item_price: Optional[Price1] = Field(default=UNSET, alias="itemPrice")
    """Competitor's item shipping price details of the item recommendation."""

    shipping_price: Optional[Price1] = Field(default=UNSET, alias="shippingPrice")
    """Competitor's item shipping price details of the item recommendation."""


class WalmartItemInfoDict(TypedDict):
    item_id: NotRequired[str]
    url: NotRequired[str]
    wfs_indicator: NotRequired[bool]
    item_price: NotRequired[Price1Dict]
    shipping_price: NotRequired[Price1Dict]
