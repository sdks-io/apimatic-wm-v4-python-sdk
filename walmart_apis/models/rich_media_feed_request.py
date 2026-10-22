from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .supplier_item_feed_header import SupplierItemFeedHeader, SupplierItemFeedHeaderDict
from .supplier_item_payload import SupplierItemPayload, SupplierItemPayloadDict


class RichMediaFeedRequest(SdkBaseModel):
    """Request body for creating, updating, or delinking rich media assets."""

    supplier_item_feed_header: SupplierItemFeedHeader = Field(alias="SupplierItemFeedHeader")
    """Metadata header for the rich media feed."""

    supplier_item: list[SupplierItemPayload] = Field(alias="SupplierItem")
    """One or multiple rich media asset details and associated items."""


class RichMediaFeedRequestDict(TypedDict):
    supplier_item_feed_header: SupplierItemFeedHeaderDict
    supplier_item: list[SupplierItemPayloadDict]
