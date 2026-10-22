from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_detail import ErrorDetail, ErrorDetailDict


class ErrorResponseError(SdkBaseModel):
    """Standardized error response envelope containing an array of error details. All error responses from the API
    follow this structure."""

    error: Optional[list[ErrorDetail]] = UNSET
    """List of error details. Typically contains a single error, but may contain multiple errors for validation
    failures."""


class ErrorResponseErrorDict(TypedDict):
    error: NotRequired[list[ErrorDetailDict]]
