from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DiagnosticPage(SdkBaseModel):
    """Pagination configuration for controlling result set size and navigation.

    **Defaults when page is not provided**: offset=0, limit=100

    Both ``offset`` and ``limit`` are required when the ``page`` object is provided."""

    offset: int = 0
    """The starting position for fetching records (0-based).

    **Constraints**: Must be zero or a positive value **Default**: 0 (when page is not provided)"""

    limit: int = 100
    """Maximum number of records to fetch per page.

    **Constraints**: Must be between 1 and 100 **Default**: 100 (when page is not provided)"""


class DiagnosticPageDict(TypedDict):
    offset: int
    limit: int
