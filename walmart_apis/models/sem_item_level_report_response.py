from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sem_item_report import SemItemReport, SemItemReportDict
from .sem_pagination import SemPagination, SemPaginationDict


class SemItemLevelReportResponse(SdkBaseModel):
    pagination: Optional[SemPagination] = UNSET
    """Pagination details"""

    data: Optional[list[SemItemReport]] = UNSET
    """List of items with performance data."""


class SemItemLevelReportResponseDict(TypedDict):
    pagination: NotRequired[SemPaginationDict]
    data: NotRequired[list[SemItemReportDict]]
