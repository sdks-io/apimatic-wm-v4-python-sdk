from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .wsr_item_data import WsrItemData, WsrItemDataDict
from .wsr_pagination import WsrPagination, WsrPaginationDict


class WsrItemReportResponse(SdkBaseModel):
    """Item report response containing item-level performance data and pagination info.

    Each record includes both campaign hierarchy identifiers and item-specific details."""

    data: Optional[list[WsrItemData]] = UNSET
    """List of item-level performance data. Empty array when no data is available for the given criteria."""

    pagination: Optional[WsrPagination] = UNSET
    """Pagination metadata for navigating through the report results.

    **Empty Response**: When no data is available, all fields will be 0."""


class WsrItemReportResponseDict(TypedDict):
    data: NotRequired[list[WsrItemDataDict]]
    pagination: NotRequired[WsrPaginationDict]
