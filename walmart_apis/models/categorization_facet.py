from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CategorizationFacet(SdkBaseModel):
    """Information of item recommendations based on the categorizationType."""

    name: Optional[str] = UNSET
    """Name of the brand or category as per the categorizationType."""

    number_of_item_recommendations: Optional[int] = Field(default=UNSET, alias="numberOfItemRecommendations")
    """The number of item recommendations associated with the name. The name can be associated with the categorization
    type."""


class CategorizationFacetDict(TypedDict):
    name: NotRequired[str]
    number_of_item_recommendations: NotRequired[int]
