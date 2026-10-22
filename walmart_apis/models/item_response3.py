from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ItemResponse3(SdkBaseModel):
    """Items status included in the list."""

    product_id: Optional[str] = Field(default=UNSET, alias="productId")
    """The Walmart Product ID assigned by Walmart to the item when it is listed on Walmart.com."""

    product_id_type: Optional[str] = Field(default=UNSET, alias="productIdType")
    """A seller-specified, alphanumeric string uniquely identifying the Product Type. Example: 'Diamond'."""

    status: Optional[str] = UNSET
    """Status of the item."""

    last_updated_date: Optional[str] = Field(default=UNSET, alias="lastUpdatedDate")
    """Date when an action was taken on the item."""


class ItemResponse3Dict(TypedDict):
    product_id: NotRequired[str]
    product_id_type: NotRequired[str]
    status: NotRequired[str]
    last_updated_date: NotRequired[str]
