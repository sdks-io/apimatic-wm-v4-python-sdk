from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class WsrPage(SdkBaseModel):
    """Pagination configuration for controlling result set size and navigation.

    The pagination uses offset-based navigation where:
    - ``offset`` = starting record position (0-indexed)
    - ``limit`` = number of records per page

    **Internal Conversion**: pageNumber = (offset / limit) + 1"""

    limit: int = 10
    """Maximum number of records to fetch per page.

    **Constraints**: Must be a positive value **Default**: 10"""

    offset: int = 0
    """The starting position for fetching records (0-indexed).

    **Important**: This is a record offset, NOT a page number.
    - ``offset=0`` returns records 1-10 (with ``limit=10``)
    - ``offset=10`` returns records 11-20 (with ``limit=10``)

    **Default**: 0"""


class WsrPageDict(TypedDict):
    limit: NotRequired[int]
    offset: NotRequired[int]
