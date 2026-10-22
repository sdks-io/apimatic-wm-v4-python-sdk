from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.category1 import Category1OrStr
from .enums.severity1 import Severity1OrStr


class Error31(SdkBaseModel):
    """Error detail object."""

    info: Optional[str] = UNSET
    """Additional contextual information about the error."""

    code: Optional[str] = UNSET
    """Error code identifying the failure reason."""

    field: Optional[str] = UNSET
    """The Name of the request field that triggered this error, when applicable."""

    description: Optional[str] = UNSET
    """Human-readable description of the error."""

    severity: Optional[Severity1OrStr] = UNSET
    """Severity level of the error."""

    category: Optional[Category1OrStr] = UNSET
    """Category classifying the origin of the error."""

    http_status: Optional[int] = Field(default=UNSET, alias="httpStatus")
    """HTTP status code associated with this error. 501 indicates the functionality is not implemented."""


class Error31Dict(TypedDict):
    info: NotRequired[str]
    code: NotRequired[str]
    field: NotRequired[str]
    description: NotRequired[str]
    severity: NotRequired[Severity1OrStr]
    category: NotRequired[Category1OrStr]
    http_status: NotRequired[int]
