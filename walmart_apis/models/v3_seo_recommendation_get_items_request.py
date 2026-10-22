from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .search_filter import SearchFilter, SearchFilterDict


class V3SeoRecommendationGetItemsRequest(SdkBaseModel):
    search_filter: Optional[SearchFilter] = Field(default=UNSET, alias="searchFilter")


class V3SeoRecommendationGetItemsRequestDict(TypedDict):
    search_filter: NotRequired[SearchFilterDict]
