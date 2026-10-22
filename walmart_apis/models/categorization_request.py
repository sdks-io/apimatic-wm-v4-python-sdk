from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .categorization_request_filter import CategorizationRequestFilter, CategorizationRequestFilterDict
from .enums.categorization_type import CategorizationTypeOrStr
from .meta_data_request import MetaDataRequest, MetaDataRequestDict


class CategorizationRequest(SdkBaseModel):
    categorization_type: CategorizationTypeOrStr = Field(alias="categorizationType")
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | BRAND | To get list of brands which are associated with the assortment recommendations | string |
    | CATEGORY | To get list of categories which are associated with the assortment recommendations | string |"""

    meta: Optional[MetaDataRequest] = UNSET
    """Meta information for the request."""

    filter_criteria: Optional[CategorizationRequestFilter] = Field(default=UNSET, alias="filterCriteria")
    """Different type of filters can be passed in this object."""


class CategorizationRequestDict(TypedDict):
    categorization_type: CategorizationTypeOrStr
    meta: NotRequired[MetaDataRequestDict]
    filter_criteria: NotRequired[CategorizationRequestFilterDict]
