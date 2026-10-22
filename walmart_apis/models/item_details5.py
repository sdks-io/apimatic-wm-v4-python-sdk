from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_ingestion_status import ItemIngestionStatus, ItemIngestionStatusDict


class ItemDetails5(SdkBaseModel):
    """List of ingestion status details for items in the feed."""

    item_ingestion_status: Optional[list[ItemIngestionStatus]] = Field(default=UNSET, alias="itemIngestionStatus")
    """The ingestion status of an individual item."""


class ItemDetails5Dict(TypedDict):
    item_ingestion_status: NotRequired[list[ItemIngestionStatusDict]]
