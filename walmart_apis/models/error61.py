from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Error61(SdkBaseModel):
    info: Optional[str] = UNSET
    """Additional contextual information about the error."""

    code: Optional[str] = UNSET
    """Error code identifying the failure reason."""

    field: Optional[str] = UNSET
    """The name of the request field that triggered this error, when applicable."""

    description: Optional[str] = UNSET
    """Human-readable description of the error."""

    severity: Optional[str] = UNSET
    """Severity level of the error."""

    category: Optional[str] = UNSET
    """Category classifying the origin of the error."""

    http_status: Optional[int] = Field(default=UNSET, alias="httpStatus")
    """HTTP status code associated with this error. 501 indicates the functionality is not implemented."""


class Error61Dict(TypedDict):
    info: NotRequired[str]
    code: NotRequired[str]
    field: NotRequired[str]
    description: NotRequired[str]
    severity: NotRequired[str]
    category: NotRequired[str]
    http_status: NotRequired[int]
