from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bulk_item_status_update_response_payload import (
    BulkItemStatusUpdateResponsePayload,
    BulkItemStatusUpdateResponsePayloadDict,
)
from .error8 import Error8, Error8Dict


class BulkItemUpdateResponse(SdkBaseModel):
    payload: Optional[BulkItemStatusUpdateResponsePayload] = UNSET
    """Response payload."""

    status_code: Optional[int] = Field(default=UNSET, alias="statusCode")
    """Status code for the request."""

    errors: Optional[list[Error8]] = UNSET


class BulkItemUpdateResponseDict(TypedDict):
    payload: NotRequired[BulkItemStatusUpdateResponsePayloadDict]
    status_code: NotRequired[int]
    errors: NotRequired[list[Error8Dict]]
