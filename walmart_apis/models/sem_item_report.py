from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sem_traffic import SemTraffic, SemTrafficDict


class SemItemReport(SdkBaseModel):
    """List of items with performance data"""

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

    status: Optional[str] = UNSET
    """Status of the item"""

    olq_score: Optional[float] = Field(default=UNSET, alias="olqScore")
    """OLQ Score of the item"""

    offer_price: Optional[float] = Field(default=UNSET, alias="offerPrice")
    """Offer Price"""

    competitor_price: Optional[float] = Field(default=UNSET, alias="competitorPrice")
    """Competitor Price"""

    google_price: Optional[float] = Field(default=UNSET, alias="googlePrice")
    """Google Price"""

    traffic: Optional[SemTraffic] = UNSET
    """Performance data of the campaign"""


class SemItemReportDict(TypedDict):
    item_id: NotRequired[str]
    sku: NotRequired[str]
    product_id: NotRequired[str]
    product_name: NotRequired[str]
    category_name: NotRequired[str]
    product_url: NotRequired[str]
    product_image_url: NotRequired[str]
    status: NotRequired[str]
    olq_score: NotRequired[float]
    offer_price: NotRequired[float]
    competitor_price: NotRequired[float]
    google_price: NotRequired[float]
    traffic: NotRequired[SemTrafficDict]
