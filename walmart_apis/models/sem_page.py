from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SemPage(SdkBaseModel):
    """Pagination criteria"""

    offset: int
    """The starting position for fetching records. Must be zero or a positive value."""

    limit: int
    """The maximum number of records to fetch per page. Must be a positive value and cannot exceed 200."""


class SemPageDict(TypedDict):
    offset: int
    limit: int
