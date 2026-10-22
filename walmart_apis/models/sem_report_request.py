from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sem_filter import SemFilter, SemFilterDict
from .sem_page import SemPage, SemPageDict
from .sem_sort import SemSort, SemSortDict


class SemReportRequest(SdkBaseModel):
    page: Optional[SemPage] = UNSET
    """Pagination criteria"""

    sort: Optional[SemSort] = UNSET
    """Sorting criteria"""

    filters: Optional[list[SemFilter]] = UNSET
    """Filtering criteria"""


class SemReportRequestDict(TypedDict):
    page: NotRequired[SemPageDict]
    sort: NotRequired[SemSortDict]
    filters: NotRequired[list[SemFilterDict]]
