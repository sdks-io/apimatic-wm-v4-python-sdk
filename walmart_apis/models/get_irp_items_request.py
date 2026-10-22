from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .filter_request import FilterRequest, FilterRequestDict
from .search_request import SearchRequest, SearchRequestDict
from .sort_request import SortRequest, SortRequestDict


class GetIrpItemsRequest(SdkBaseModel):
    search: Optional[list[SearchRequest]] = UNSET
    """Search request."""

    filter: FilterRequest
    """Filter request."""

    sort: Optional[list[SortRequest]] = UNSET
    """Sort request."""


class GetIrpItemsRequestDict(TypedDict):
    search: NotRequired[list[SearchRequestDict]]
    filter: FilterRequestDict
    sort: NotRequired[list[SortRequestDict]]
