from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item3 import Item3, Item3Dict


class V3SeoRecommendationGetItems500Error1(SdkBaseModel):
    error: Optional[str] = UNSET
    next_cursor: Optional[str] = UNSET
    """The link to the next scrollID to be used for pagination"""

    previous_cursor: Optional[str] = UNSET
    """The link to the previously used scrollID if one was provided."""

    total_records: Optional[int] = UNSET
    """The total number of records available regardless of state"""

    records_fetched: Optional[int] = UNSET
    """The number of records fetched according to the search filters"""

    items: Optional[list[Item3]] = UNSET


class V3SeoRecommendationGetItems500Error1Dict(TypedDict):
    error: NotRequired[str]
    next_cursor: NotRequired[str]
    previous_cursor: NotRequired[str]
    total_records: NotRequired[int]
    records_fetched: NotRequired[int]
    items: NotRequired[list[Item3Dict]]
