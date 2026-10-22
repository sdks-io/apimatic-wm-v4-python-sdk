from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error12 import Error12, Error12Dict
from .payload51 import Payload51, Payload51Dict


class V3GrowthReviewsAcceleratorCategoriesResponse(SdkBaseModel):
    payload: Optional[Payload51] = UNSET
    """Response payload."""

    status_code: Optional[int] = Field(default=UNSET, alias="statusCode")
    """Status code for the request.<br><b style='color:green;'>Market availability: US only</b>"""

    errors: Optional[list[Error12]] = UNSET


class V3GrowthReviewsAcceleratorCategoriesResponseDict(TypedDict):
    payload: NotRequired[Payload51Dict]
    status_code: NotRequired[int]
    errors: NotRequired[list[Error12Dict]]
