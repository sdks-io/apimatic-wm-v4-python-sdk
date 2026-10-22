from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .insight2 import Insight2, Insight2Dict


class RecommendedItem2(SdkBaseModel):
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

    item_condition: Optional[str] = Field(default=UNSET, alias="itemCondition")
    """The item's condition described by its appearance, quality, packaging, functionality, and previous usage."""

    units_stored: Optional[int] = Field(default=UNSET, alias="unitsStored")
    """The estimated number of units per item currently in stock at WFS fulfillment centers."""

    publishing_status: Optional[str] = Field(default=UNSET, alias="publishingStatus")
    """The overall status of the item in your Walmart Marketplace catalog. Available statuses include: Published,
    Unpublished, Processing, Stage, Error, or WFS Ineligible."""

    insights: Optional[list[Insight2]] = UNSET


class RecommendedItem2Dict(TypedDict):
    gtin: NotRequired[str]
    sku: NotRequired[str]
    item_id: NotRequired[str]
    brand: NotRequired[str]
    item_name: NotRequired[str]
    item_condition: NotRequired[str]
    units_stored: NotRequired[int]
    publishing_status: NotRequired[str]
    insights: NotRequired[list[Insight2Dict]]
