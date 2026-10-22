from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data3 import Data3, Data3Dict
from .error_response4 import ErrorResponse4, ErrorResponse4Dict


class CommonResponseListCarrierPackageResponse(SdkBaseModel):
    data: Optional[list[Data3]] = UNSET
    """List of supported carrier package types."""

    errors: Optional[list[ErrorResponse4]] = UNSET
    """List of error details describing why the request failed."""


class CommonResponseListCarrierPackageResponseDict(TypedDict):
    data: NotRequired[list[Data3Dict]]
    errors: NotRequired[list[ErrorResponse4Dict]]
