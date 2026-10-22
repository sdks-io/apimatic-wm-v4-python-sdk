from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .multi_value_filter7 import MultiValueFilter7, MultiValueFilter7Dict


class FilterCriteria4(SdkBaseModel):
    """Different type of filters can be passed in this object.<br><b style='color:green;'>Market availability: US | CA |
    MX</span></b>"""

    search_text: Optional[str] = Field(default=UNSET, alias="searchText")
    """To filter with a search text having a word that can be part of the categorization data. <br><b
    style='color:green;'>Market availability: US | CA | MX</span></b>"""

    multi_value_filter: Optional[list[MultiValueFilter7]] = Field(default=UNSET, alias="multiValueFilter")
    """Filters based on multiple values associated with a specific parameter. No parameter should be repeated."""


class FilterCriteria4Dict(TypedDict):
    search_text: NotRequired[str]
    multi_value_filter: NotRequired[list[MultiValueFilter7Dict]]
