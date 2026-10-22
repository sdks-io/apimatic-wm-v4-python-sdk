from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data1 import Data1, Data1Dict
from .error_response4 import ErrorResponse4, ErrorResponse4Dict


class CommonResponseLabelGenerationResponse(SdkBaseModel):
    data: Optional[Data1] = UNSET
    """Response payload containing the generated label tracking details."""

    errors: Optional[list[ErrorResponse4]] = UNSET
    """List of error details describing why the request failed."""


class CommonResponseLabelGenerationResponseDict(TypedDict):
    data: NotRequired[Data1Dict]
    errors: NotRequired[list[ErrorResponse4Dict]]
