from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.date_range import DateRange, DateRangeOrStr
from .enums.item_status3 import ItemStatus3OrStr
from .price_request import PriceRequest, PriceRequestDict


class FilterRequest(SdkBaseModel):
    """Filter request."""

    item_status: ItemStatus3OrStr = Field(alias="itemStatus")
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ELIGIBLE | To get items which are eligible for the program | string |
    | ENROLLED | To get items which are currently enrolled into the program | string |
    | COMPLETE | To get items which have attained target reviews through the program | string |"""

    date_range: DateRangeOrStr = Field(default=DateRange._7_DAYS, alias="dateRange")
    """Date range to filter impressions, page views, and sales."""

    category: Optional[str] = UNSET
    """Category of the items."""

    price: Optional[PriceRequest] = UNSET
    """Price range of the items."""


class FilterRequestDict(TypedDict):
    item_status: ItemStatus3OrStr
    date_range: NotRequired[DateRangeOrStr]
    category: NotRequired[str]
    price: NotRequired[PriceRequestDict]
