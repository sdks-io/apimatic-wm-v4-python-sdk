from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error12 import Error12, Error12Dict
from .payload41 import Payload41, Payload41Dict


class V3GrowthReviewsAcceleratorItemsResponse(SdkBaseModel):
    payload: Optional[Payload41] = UNSET
    """Response payload."""

    status_code: Optional[int] = Field(default=UNSET, alias="statusCode")
    """Status code for the request.<br><b style='color:green;'>Market availability: US only</b>"""

    errors: Optional[list[Error12]] = UNSET


class V3GrowthReviewsAcceleratorItemsResponseDict(TypedDict):
    payload: NotRequired[Payload41Dict]
    status_code: NotRequired[int]
    errors: NotRequired[list[Error12Dict]]
