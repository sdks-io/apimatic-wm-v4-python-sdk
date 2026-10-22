from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta_data_request import MetaDataRequest, MetaDataRequestDict
from .recommendation_request_filter import RecommendationRequestFilter, RecommendationRequestFilterDict


class RecommendationRequest(SdkBaseModel):
    recommendation_type: Literal["ITEM"] = Field(default="ITEM", alias="recommendationType")
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ITEM | To get list of recommended items | string |"""

    meta: Optional[MetaDataRequest] = UNSET
    """Meta information for the request."""

    filter_criteria: Optional[RecommendationRequestFilter] = Field(default=UNSET, alias="filterCriteria")
    """Different type of filters can be passed in this object."""


class RecommendationRequestDict(TypedDict):
    recommendation_type: Literal["ITEM"]
    meta: NotRequired[MetaDataRequestDict]
    filter_criteria: NotRequired[RecommendationRequestFilterDict]
