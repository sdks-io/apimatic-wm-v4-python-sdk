from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .multi_value_filter_criteria_for_categorization import (
    MultiValueFilterCriteriaForCategorization,
    MultiValueFilterCriteriaForCategorizationDict,
)


class CategorizationRequestFilter(SdkBaseModel):
    """Different type of filters can be passed in this object."""

    search_text: Optional[str] = Field(default=UNSET, alias="searchText")
    """To filter with a search text having a word that can be part of the categorization data."""

    multi_value_filter: Optional[list[MultiValueFilterCriteriaForCategorization]] = Field(
        default=UNSET, alias="multiValueFilter"
    )
    """Filters based on multiple values associated with a specific parameter. No parameter should be repeated."""


class CategorizationRequestFilterDict(TypedDict):
    search_text: NotRequired[str]
    multi_value_filter: NotRequired[list[MultiValueFilterCriteriaForCategorizationDict]]
