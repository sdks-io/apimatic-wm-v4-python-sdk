from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error8 import Error8, Error8Dict
from .get_categories_response_payload import GetCategoriesResponsePayload, GetCategoriesResponsePayloadDict


class GetCategoriesResponse1(SdkBaseModel):
    payload: Optional[GetCategoriesResponsePayload] = UNSET
    """Response payload."""

    status_code: Optional[int] = Field(default=UNSET, alias="statusCode")
    """Status code for the request."""

    errors: Optional[list[Error8]] = UNSET


class GetCategoriesResponse1Dict(TypedDict):
    payload: NotRequired[GetCategoriesResponsePayloadDict]
    status_code: NotRequired[int]
    errors: NotRequired[list[Error8Dict]]
