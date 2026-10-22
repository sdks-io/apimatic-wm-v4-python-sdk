from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DiagnosticPagination(SdkBaseModel):
    """Pagination metadata for navigating through search results.

    Includes ``hasNextPage`` and ``hasPreviousPage`` boolean flags for convenient pagination control in UIs."""

    page_no: Optional[int] = Field(default=UNSET, alias="pageNo")
    """Current page number (0-based). Calculated as: offset / limit"""

    page_size: Optional[int] = Field(default=UNSET, alias="pageSize")
    """Number of items per page (same as ``limit`` in request)."""

    total_count: Optional[int] = Field(default=UNSET, alias="totalCount")
    """Total number of items matching the search criteria across all pages."""

    total_pages: Optional[int] = Field(default=UNSET, alias="totalPages")
    """Total number of pages available. Calculated as: ceil(totalCount / pageSize)"""

    has_next_page: Optional[bool] = Field(default=UNSET, alias="hasNextPage")
    """``true`` if more pages exist after the current page."""

    has_previous_page: Optional[bool] = Field(default=UNSET, alias="hasPreviousPage")
    """``true`` if pages exist before the current page."""


class DiagnosticPaginationDict(TypedDict):
    page_no: NotRequired[int]
    page_size: NotRequired[int]
    total_count: NotRequired[int]
    total_pages: NotRequired[int]
    has_next_page: NotRequired[bool]
    has_previous_page: NotRequired[bool]
