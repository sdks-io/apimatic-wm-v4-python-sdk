from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .wsr_error_detail import WsrErrorDetail, WsrErrorDetailDict


class WsrErrorResponse(SdkBaseModel):
    """Error response wrapper containing an array of errors"""

    errors: Optional[list[WsrErrorDetail]] = UNSET
    """List of error details"""


class WsrErrorResponseDict(TypedDict):
    errors: NotRequired[list[WsrErrorDetailDict]]
