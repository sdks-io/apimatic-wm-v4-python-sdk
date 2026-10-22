from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enum_filter4 import EnumFilter4, EnumFilter4Dict
from .multi_value_filter6 import MultiValueFilter6, MultiValueFilter6Dict
from .range_filter3 import RangeFilter3, RangeFilter3Dict


class FilterCriteria3(SdkBaseModel):
    """Different type of filters can be passed in this object."""

    search_text: Optional[str] = Field(default=UNSET, alias="searchText")
    """To filter with a search text having a word that can be part of the recommended data.
     searchText for US 'and', for CA and MX 'Rio'. <br><b style='color:green;'>Market availability: US | CA |
        MX</span></b>"""

    multi_value_filter: Optional[list[MultiValueFilter6]] = Field(default=UNSET, alias="multiValueFilter")
    """Filters based on multiple values associated with a specific parameter. No parameter should be repeated. <br><b
    style='color:green;'>Market availability: US | CA | MX</span></b>"""

    enum_filter: Optional[list[EnumFilter4]] = Field(default=UNSET, alias="enumFilter")
    """Filter based on preset parameters and their associated values is possible with EnumFilter. No parameter should be
    repeated. <br><b style='color:green;'>Market availability: US only</span></b>"""

    range_filter: Optional[list[RangeFilter3]] = Field(default=UNSET, alias="rangeFilter")
    """Filter based on a range with ``RangeFilter``. You must also pass a parameter along with any of the beginning or
    the ending points or both. No parameter should be repeated.<br><b style='color:green;'>Market availability: US | CA
    | MX</span></b>"""

    is_top_go_get_item: Optional[bool] = Field(default=UNSET, alias="isTopGoGetItem")
    """Filters the Top Go-Get Items, which are high-demand, customer-favorite items that sellers should prioritize
    adding to their Walmart catalog. Set to ``true`` to return only Top Go-Get Items. <br><b style='color:green;'>Market
    availability: US | CA | MX</span></b>"""

    is_new_recommendation: Optional[bool] = Field(default=UNSET, alias="isNewRecommendation")
    """Filter for newly added recommendations. These are high-demand, customer-favorite items added to the
    recommendation set within the past 30 days. Set to ``true`` to return only these items. <br><b
    style='color:green;'>Market availability: US | CA | MX</span></b>"""


class FilterCriteria3Dict(TypedDict):
    search_text: NotRequired[str]
    multi_value_filter: NotRequired[list[MultiValueFilter6Dict]]
    enum_filter: NotRequired[list[EnumFilter4Dict]]
    range_filter: NotRequired[list[RangeFilter3Dict]]
    is_top_go_get_item: NotRequired[bool]
    is_new_recommendation: NotRequired[bool]
