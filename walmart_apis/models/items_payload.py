from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.item_status import ItemStatusOrStr


class ItemsPayload(SdkBaseModel):
    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    """Specifies the item identifier."""

    item_name: Optional[str] = Field(default=UNSET, alias="itemName")
    """Name of the item."""

    sales: OptionalNullable[int] = UNSET
    """Units sold during the specified date range. The default date range is the last 7 days. May be null when data is
    unavailable for the item."""

    current_reviews: Optional[int] = Field(default=UNSET, alias="currentReviews")
    """Current number of reviews on the item."""

    impressions: OptionalNullable[int] = UNSET
    """The number of times the item appeared in search results during the specified date range. The default date range
    is the last 7 days. May be null when data is unavailable for the item."""

    current_page_views: OptionalNullable[int] = Field(default=UNSET, alias="currentPageViews")
    """The number of views on the item page during the specified date range. The default date range is the last 7 days.
    May be null when data is unavailable for the item."""

    reviews_collected: Optional[int] = Field(default=UNSET, alias="reviewsCollected")
    """The number of reviews collected for the item through IRP."""

    sku: Optional[str] = UNSET
    """Represents the Stock Keeping Unit (SKU), which is a unique identifier as defined by the seller. This identifier
    helps in tracking inventory and managing items efficiently."""

    item_status: Optional[ItemStatusOrStr] = Field(default=UNSET, alias="itemStatus")
    """Current status of the item in IRP."""

    item_priority: Optional[int] = Field(default=UNSET, alias="itemPriority")
    """Priority of the item as recommended by Walmart."""


class ItemsPayloadDict(TypedDict):
    item_id: NotRequired[str]
    item_name: NotRequired[str]
    sales: NotRequired[int | None]
    current_reviews: NotRequired[int]
    impressions: NotRequired[int | None]
    current_page_views: NotRequired[int | None]
    reviews_collected: NotRequired[int]
    sku: NotRequired[str]
    item_status: NotRequired[ItemStatusOrStr]
    item_priority: NotRequired[int]
