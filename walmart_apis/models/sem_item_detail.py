from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SemItemDetail(SdkBaseModel):
    """List of item details included in the catalog response."""

    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    """A unique ID which identifies the item."""

    sku: Optional[str] = UNSET
    """An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item."""

    product_id: Optional[str] = Field(default=UNSET, alias="productId")
    """Product ID of the item"""

    product_name: Optional[str] = Field(default=UNSET, alias="productName")
    """A seller-specified, alphanumeric string uniquely identifying the product name."""

    category_name: Optional[str] = Field(default=UNSET, alias="categoryName")
    """Category of the item."""

    product_url: Optional[str] = Field(default=UNSET, alias="productUrl")
    """URL where the item can be viewed."""

    product_image_url: Optional[str] = Field(default=UNSET, alias="productImageUrl")
    """URL of the image representing the item."""

    recommendation_type: Optional[str] = Field(default=UNSET, alias="recommendationType")
    """Recommendation type for the item, indicating how it is recommended for SEM campaigns."""


class SemItemDetailDict(TypedDict):
    item_id: NotRequired[str]
    sku: NotRequired[str]
    product_id: NotRequired[str]
    product_name: NotRequired[str]
    category_name: NotRequired[str]
    product_url: NotRequired[str]
    product_image_url: NotRequired[str]
    recommendation_type: NotRequired[str]
