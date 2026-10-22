from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error12 import Error12, Error12Dict
from .payload32 import Payload32, Payload32Dict


class V3GrowthReviewsAcceleratorItemsStatusResponse(SdkBaseModel):
    payload: Optional[Payload32] = UNSET
    """Response payload."""

    status_code: Optional[int] = Field(default=UNSET, alias="statusCode")
    """Status code for the request."""

    errors: Optional[list[Error12]] = UNSET


class V3GrowthReviewsAcceleratorItemsStatusResponseDict(TypedDict):
    payload: NotRequired[Payload32Dict]
    status_code: NotRequired[int]
    errors: NotRequired[list[Error12Dict]]
