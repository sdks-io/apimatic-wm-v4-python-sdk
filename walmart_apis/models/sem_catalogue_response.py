from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sem_item_detail import SemItemDetail, SemItemDetailDict
from .sem_pagination import SemPagination, SemPaginationDict


class SemCatalogueResponse(SdkBaseModel):
    pagination: Optional[SemPagination] = UNSET
    """Pagination details"""

    data: Optional[list[SemItemDetail]] = UNSET
    """List of item details included in the catalog response."""


class SemCatalogueResponseDict(TypedDict):
    pagination: NotRequired[SemPaginationDict]
    data: NotRequired[list[SemItemDetailDict]]
