from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Replenishment(SdkBaseModel):
    item_id: str = Field(alias="itemId")
    """The Walmart-assigned ID used to track items. This ID is located at the end of the item page URL."""

    gtin: str
    """The Global Trade Identification Number (GTIN) associated with the item. If you provide a 12-digit UPC rather than
    a GTIN, the GTIN will start with two 0s followed by the UPC."""

    upc: Optional[str] = UNSET
    """Universal Product Code (UPC) of the item."""

    vendor_sku: str = Field(alias="vendorSku")
    """The unique identifier assigned to the item by the seller."""

    max_qty: int = Field(alias="maxQty")
    """Recommended maximum quantity for the item"""

    suggested_qty: Optional[int] = Field(default=UNSET, alias="suggestedQty")
    """Suggested inbound quantity"""

    customer_favorite: Optional[bool] = Field(default=UNSET, alias="customerFavorite")
    """Indicates whether the item is identified as a customer favorite based on customer demand."""


class ReplenishmentDict(TypedDict):
    item_id: str
    gtin: str
    upc: NotRequired[str]
    vendor_sku: str
    max_qty: int
    suggested_qty: NotRequired[int]
    customer_favorite: NotRequired[bool]
