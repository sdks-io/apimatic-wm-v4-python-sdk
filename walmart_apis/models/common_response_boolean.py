from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_response4 import ErrorResponse4, ErrorResponse4Dict


class CommonResponseBoolean(SdkBaseModel):
    data: Optional[bool] = UNSET
    """Returns ``true`` if the operation was successful, ``false`` otherwise."""

    errors: Optional[list[ErrorResponse4]] = UNSET
    """List of error details describing why the request failed."""


class CommonResponseBooleanDict(TypedDict):
    data: NotRequired[bool]
    errors: NotRequired[list[ErrorResponse4Dict]]
