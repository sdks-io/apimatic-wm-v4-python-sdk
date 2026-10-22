from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data2 import Data2, Data2Dict
from .error_response4 import ErrorResponse4, ErrorResponse4Dict


class CommonResponseListLabelGenerationResponse(SdkBaseModel):
    data: Optional[list[Data2]] = UNSET
    """List of label details generated for the specified purchase order ID."""

    errors: Optional[list[ErrorResponse4]] = UNSET
    """List of error details describing why the request failed."""


class CommonResponseListLabelGenerationResponseDict(TypedDict):
    data: NotRequired[list[Data2Dict]]
    errors: NotRequired[list[ErrorResponse4Dict]]
