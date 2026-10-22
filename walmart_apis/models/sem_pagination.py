from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SemPagination(SdkBaseModel):
    """Pagination details"""

    page_no: Optional[int] = Field(default=UNSET, alias="pageNo")
    """Page number."""

    page_size: Optional[int] = Field(default=UNSET, alias="pageSize")
    """Page size"""

    total_count: Optional[int] = Field(default=UNSET, alias="totalCount")
    """Total count"""

    total_pages: Optional[int] = Field(default=UNSET, alias="totalPages")
    """Total pages"""


class SemPaginationDict(TypedDict):
    page_no: NotRequired[int]
    page_size: NotRequired[int]
    total_count: NotRequired[int]
    total_pages: NotRequired[int]
