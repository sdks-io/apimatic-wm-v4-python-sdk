from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ItemsSuccessResponse(SdkBaseModel):
    """Items."""

    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    """Specifies the item identifier."""

    item_description: Optional[str] = Field(default=UNSET, alias="itemDescription")
    """Description of the item."""

    sku: Optional[str] = UNSET
    """Represents the Stock Keeping Unit (SKU), which is a unique identifier as defined by the seller. This identifier
    helps in tracking inventory and managing items efficiently."""


class ItemsSuccessResponseDict(TypedDict):
    item_id: NotRequired[str]
    item_description: NotRequired[str]
    sku: NotRequired[str]
