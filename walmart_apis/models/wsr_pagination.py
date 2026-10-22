from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WsrPagination(SdkBaseModel):
    """Pagination metadata for navigating through the report results.

    **Empty Response**: When no data is available, all fields will be 0."""

    page_no: Optional[int] = Field(default=UNSET, alias="pageNo")
    """Current page number (1-indexed). Value is 0 when no data is available."""

    page_size: Optional[int] = Field(default=UNSET, alias="pageSize")
    """Number of records per page (same as limit in request). Value is 0 when no data is available."""

    total_count: Optional[int] = Field(default=UNSET, alias="totalCount")
    """Total number of records available across all pages"""

    total_pages: Optional[int] = Field(default=UNSET, alias="totalPages")
    """Total number of pages available"""


class WsrPaginationDict(TypedDict):
    page_no: NotRequired[int]
    page_size: NotRequired[int]
    total_count: NotRequired[int]
    total_pages: NotRequired[int]
