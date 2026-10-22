from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enum_filter1 import EnumFilter1, EnumFilter1Dict
from .multi_value_filter import MultiValueFilter, MultiValueFilterDict
from .range_filter_criteria import RangeFilterCriteria, RangeFilterCriteriaDict


class RecommendationRequestFilter(SdkBaseModel):
    """Different type of filters can be passed in this object."""

    search_text: Optional[str] = Field(default=UNSET, alias="searchText")
    """To filter with a search text having a word that can be part of the recommended data."""

    multi_value_filter: Optional[list[MultiValueFilter]] = Field(default=UNSET, alias="multiValueFilter")
    """Filters based on multiple values associated with a specific parameter. No parameter should be repeated."""

    enum_filter: Optional[list[EnumFilter1]] = Field(default=UNSET, alias="enumFilter")
    """Filter based on preset parameters and their associated values is possible with EnumFilter. No parameter should be
    repeated."""

    range_filter: Optional[list[RangeFilterCriteria]] = Field(default=UNSET, alias="rangeFilter")
    """Filter based on a range with RangeFilter. You must also pass a parameter along with any of the beginning or the
    ending points or both. No parameter should be repeated."""

    is_top_go_get_item: Optional[bool] = Field(default=UNSET, alias="isTopGoGetItem")
    """Filters the Top Go-Get Items, which are high-demand, customer-favorite items that sellers should prioritize
    adding to their Walmart catalog. Set to ``true`` to return only Top Go-Get Items."""

    is_new_recommendation: Optional[bool] = Field(default=UNSET, alias="isNewRecommendation")
    """Filter for newly added recommendations. These are high-demand, customer-favorite items added to the
    recommendation set within the past 30 days. Set to ``true`` to return only these items."""


class RecommendationRequestFilterDict(TypedDict):
    search_text: NotRequired[str]
    multi_value_filter: NotRequired[list[MultiValueFilterDict]]
    enum_filter: NotRequired[list[EnumFilter1Dict]]
    range_filter: NotRequired[list[RangeFilterCriteriaDict]]
    is_top_go_get_item: NotRequired[bool]
    is_new_recommendation: NotRequired[bool]
