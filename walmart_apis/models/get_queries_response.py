from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pagination1 import Pagination1, Pagination1Dict
from .query import Query, QueryDict


class GetQueriesResponse(SdkBaseModel):
    queries: Optional[list[Query]] = UNSET
    pagination: Optional[Pagination1] = UNSET


class GetQueriesResponseDict(TypedDict):
    queries: NotRequired[list[Query | QueryDict]]
    pagination: NotRequired[Pagination1 | Pagination1Dict]
