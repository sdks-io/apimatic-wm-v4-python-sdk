from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.date_range4 import DateRange4, DateRange4OrStr
from .enums.item_status8 import ItemStatus8OrStr
from .price22 import Price22, Price22Dict


class Filter1(SdkBaseModel):
    """Specifies the filter request.<br><b style='color:green;'>Market availability: US only</b>"""

    item_status: ItemStatus8OrStr = Field(alias="itemStatus")
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ELIGIBLE | To get items which are eligible for the program | string |
    | ENROLLED | To get items which are currently enrolled into the program | string |
    | COMPLETE | To get items which have attained target reviews through the program | string |
    <br><b style='color:green;'>Market availability: US only</b>"""

    date_range: DateRange4OrStr = Field(default=DateRange4._7_DAYS, alias="dateRange")
    """Date range to filter impressions, page views, and sales.<br><b style='color:green;'>Market availability: US
    only</b>"""

    category: Optional[list[str]] = UNSET
    """Category of the items."""

    price: Optional[Price22] = UNSET
    """Price range of the items.<br><b style='color:green;'>Market availability: US only</b>"""

    is_customer_favorite: Optional[bool] = Field(default=UNSET, alias="isCustomerFavorite")
    """Filter items by customer favorite status. Set to true to return only customer favorite items. Set to false to
    return only non-customer favorite items. If omitted, all items are returned regardless of customer favorite
    status.<br><b style='color:green;'>Market availability: US only</b>"""


class Filter1Dict(TypedDict):
    item_status: ItemStatus8OrStr
    date_range: NotRequired[DateRange4OrStr]
    category: NotRequired[list[str]]
    price: NotRequired[Price22Dict]
    is_customer_favorite: NotRequired[bool]
