from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.date_range4 import DateRange4, DateRange4OrStr
from .item121 import Item121, Item121Dict


class Payload41(SdkBaseModel):
    """Response payload."""

    total_items: Optional[int] = Field(default=UNSET, alias="totalItems")
    """The total number of items found.<br><b style='color:green;'>Market availability: US only</b>"""

    fetched_items: Optional[int] = Field(default=UNSET, alias="fetchedItems")
    """The total number of items fetched.<br><b style='color:green;'>Market availability: US only</b>"""

    date_range: DateRange4OrStr = Field(default=DateRange4._7_DAYS, alias="dateRange")
    """Date range to filter impressions, page views, and sales.<br><b style='color:green;'>Market availability: US
    only</b>"""

    items: Optional[list[Item121]] = UNSET
    scroll_id: Optional[str] = Field(default=UNSET, alias="scrollId")
    """Specifies the searchId to fetch the subsequent set of results.<br><b style='color:green;'>Market availability: US
    only</b>"""


class Payload41Dict(TypedDict):
    total_items: NotRequired[int]
    fetched_items: NotRequired[int]
    date_range: NotRequired[DateRange4OrStr]
    items: NotRequired[list[Item121Dict]]
    scroll_id: NotRequired[str]
