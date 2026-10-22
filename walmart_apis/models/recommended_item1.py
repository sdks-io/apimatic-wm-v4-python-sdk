from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .insight1 import Insight1, Insight1Dict


class RecommendedItem1(SdkBaseModel):
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

    insights: Optional[list[Insight1]] = UNSET


class RecommendedItem1Dict(TypedDict):
    gtin: NotRequired[str]
    sku: NotRequired[str]
    item_id: NotRequired[str]
    brand: NotRequired[str]
    item_name: NotRequired[str]
    insights: NotRequired[list[Insight1Dict]]
