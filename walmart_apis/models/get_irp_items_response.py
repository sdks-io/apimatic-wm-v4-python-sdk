from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error8 import Error8, Error8Dict
from .get_irp_items_response_payload import GetIrpItemsResponsePayload, GetIrpItemsResponsePayloadDict


class GetIrpItemsResponse(SdkBaseModel):
    payload: Optional[GetIrpItemsResponsePayload] = UNSET
    """Response payload."""

    status_code: Optional[int] = Field(default=UNSET, alias="statusCode")
    """Status code for the request."""

    errors: Optional[list[Error8]] = UNSET


class GetIrpItemsResponseDict(TypedDict):
    payload: NotRequired[GetIrpItemsResponsePayloadDict]
    status_code: NotRequired[int]
    errors: NotRequired[list[Error8Dict]]
