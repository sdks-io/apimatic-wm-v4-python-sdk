from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.date_range import DateRange, DateRangeOrStr
from .items_payload import ItemsPayload, ItemsPayloadDict


class GetIrpItemsResponsePayload(SdkBaseModel):
    """Response payload."""

    total_items: Optional[int] = Field(default=UNSET, alias="totalItems")
    """The total of items found."""

    fetched_items: Optional[int] = Field(default=UNSET, alias="fetchedItems")
    """The total of items fetched."""

    date_range: DateRangeOrStr = Field(default=DateRange._7_DAYS, alias="dateRange")
    """Date range to filter impressions, page views, and sales."""

    items: Optional[list[ItemsPayload]] = UNSET
    scroll_id: Optional[str] = Field(default=UNSET, alias="scrollId")
    """Specifies the searchId to fetch the subsequent set of results."""


class GetIrpItemsResponsePayloadDict(TypedDict):
    total_items: NotRequired[int]
    fetched_items: NotRequired[int]
    date_range: NotRequired[DateRangeOrStr]
    items: NotRequired[list[ItemsPayloadDict]]
    scroll_id: NotRequired[str]
