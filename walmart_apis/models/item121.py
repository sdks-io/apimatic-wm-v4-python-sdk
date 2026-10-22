from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.item_status9 import ItemStatus9OrStr


class Item121(SdkBaseModel):
    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    """Specifies the item identifier.<br><b style='color:green;'>Market availability: US only</b>"""

    item_name: Optional[str] = Field(default=UNSET, alias="itemName")
    """Name of the item.<br><b style='color:green;'>Market availability: US only</b>"""

    sales: OptionalNullable[int] = UNSET
    """Units sold during the specified date range. The default date range is the last 7 days. May be null when data is
    unavailable for the item.<br><b style='color:green;'>Market availability: US only</b>"""

    current_reviews: Optional[int] = Field(default=UNSET, alias="currentReviews")
    """Current number of reviews on the item.<br><b style='color:green;'>Market availability: US only</b>"""

    impressions: OptionalNullable[int] = UNSET
    """The number of times the item appeared in search results during the specified date range. The default date range
    is the last 7 days. May be null when data is unavailable for the item.<br><b style='color:green;'>Market
    availability: US only</b>"""

    current_page_views: OptionalNullable[int] = Field(default=UNSET, alias="currentPageViews")
    """The number of views on the item page during the specified date range. The default date range is the last 7 days.
    May be null when data is unavailable for the item.<br><b style='color:green;'>Market availability: US only</b>"""

    reviews_collected: Optional[int] = Field(default=UNSET, alias="reviewsCollected")
    """The number of reviews collected for the item through IRP.<br><b style='color:green;'>Market availability: US
    only</b>"""

    sku: Optional[str] = UNSET
    """Represents the Stock Keeping Unit (SKU), which is a unique identifier as defined by the seller. This identifier
    helps in tracking inventory and managing items efficiently.<br><b style='color:green;'>Market availability: US
    only</b>"""

    item_status: Optional[ItemStatus9OrStr] = Field(default=UNSET, alias="itemStatus")
    """Current status of the item in IRP.<br><b style='color:green;'>Market availability: US only</b>"""

    item_priority: Optional[int] = Field(default=UNSET, alias="itemPriority")
    """Priority of the item as recommended by Walmart.<br><b style='color:green;'>Market availability: US only</b>"""

    is_customer_favorite: OptionalNullable[bool] = Field(default=UNSET, alias="isCustomerFavorite")
    """Indicates whether the item is a customer favorite. When the isCustomerFavorite request filter is omitted, this
    field may be true, false, or null depending on available item data. When the filter is provided, only items matching
    the filter value are returned (true returns only customer favorites; false returns only non-customer
    favorites).<br><b style='color:green;'>Market availability: US only</b>"""


class Item121Dict(TypedDict):
    item_id: NotRequired[str]
    item_name: NotRequired[str]
    sales: NotRequired[int | None]
    current_reviews: NotRequired[int]
    impressions: NotRequired[int | None]
    current_page_views: NotRequired[int | None]
    reviews_collected: NotRequired[int]
    sku: NotRequired[str]
    item_status: NotRequired[ItemStatus9OrStr]
    item_priority: NotRequired[int]
    is_customer_favorite: NotRequired[bool | None]
