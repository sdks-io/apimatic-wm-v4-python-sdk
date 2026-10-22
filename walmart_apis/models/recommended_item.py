from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .insight import Insight, InsightDict


class RecommendedItem(SdkBaseModel):
    gtin: Optional[str] = UNSET
    """The Global Trade Identification Number (GTIN) associated with the item. If you provide a 12-digit UPC rather than
    a GTIN, the GTIN will start with two 0s followed by the UPC."""

    sku: Optional[str] = UNSET
    """The unique identifier you as the seller have assigned to your item."""

    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    """Unique identifier assigned by Walmart for each item."""

    brand: Optional[str] = UNSET
    """The company name or manufacturer of the item."""

    item_name: Optional[str] = Field(default=UNSET, alias="itemName")
    """The name of the item."""

    stock_status: Optional[str] = Field(default=UNSET, alias="stockStatus")
    """Out-of-stock items have 0 units available to sell. At-risk items have fewer than 28 days of supply, including
    both available and inbound units. In-stock items have more than 28 days of total supply. Long term out of stock
    items that have been consistently out of stock for more than 30 days. New to WFS items that have been set up in WFS
    but haven't been inbounded because a shipment order has not been created."""

    item_condition: Optional[str] = Field(default=UNSET, alias="itemCondition")
    """The item's condition described by its appearance, quality, packaging, functionality, and previous usage."""

    insights: Optional[list[Insight]] = UNSET


class RecommendedItemDict(TypedDict):
    gtin: NotRequired[str]
    sku: NotRequired[str]
    item_id: NotRequired[str]
    brand: NotRequired[str]
    item_name: NotRequired[str]
    stock_status: NotRequired[str]
    item_condition: NotRequired[str]
    insights: NotRequired[list[InsightDict]]
