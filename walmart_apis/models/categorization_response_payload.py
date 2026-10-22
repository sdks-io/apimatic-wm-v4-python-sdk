from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .categorization_facet import CategorizationFacet, CategorizationFacetDict
from .enums.categorization_type import CategorizationTypeOrStr
from .meta_data_response import MetaDataResponse, MetaDataResponseDict


class CategorizationResponsePayload(SdkBaseModel):
    """Payload in the response having the categorization details about the item recommendations."""

    categorization_type: Optional[CategorizationTypeOrStr] = Field(default=UNSET, alias="categorizationType")
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | BRAND | To get list of brands which are associated with the assortment recommendations | string |
    | CATEGORY | To get list of categories which are associated with the assortment recommendations | string |"""

    meta: Optional[MetaDataResponse] = UNSET
    """Meta information for the response."""

    records: Optional[list[CategorizationFacet]] = UNSET
    """Information of item recommendations based on the categorizationType."""


class CategorizationResponsePayloadDict(TypedDict):
    categorization_type: NotRequired[CategorizationTypeOrStr]
    meta: NotRequired[MetaDataResponseDict]
    records: NotRequired[list[CategorizationFacetDict]]
