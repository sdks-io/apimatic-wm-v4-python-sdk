from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_detail429 import ErrorDetail429, ErrorDetail429Dict


class ErrorResponse429(SdkBaseModel):
    """Error response envelope for rate limit (429) errors returned by the API Gateway."""

    error: Optional[list[ErrorDetail429]] = UNSET
    """List of rate limit error details."""


class ErrorResponse429Dict(TypedDict):
    error: NotRequired[list[ErrorDetail429Dict]]
