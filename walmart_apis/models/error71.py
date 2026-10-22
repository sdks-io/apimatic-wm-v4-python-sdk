from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Error71(SdkBaseModel):
    info: Optional[str] = UNSET
    code: Optional[str] = UNSET
    field: Optional[str] = UNSET
    description: Optional[str] = UNSET
    severity: Optional[str] = UNSET
    category: Optional[str] = UNSET
    http_status: Optional[int] = Field(default=UNSET, alias="httpStatus")
    """HTTP status code for this error, 501 indicates the functionality is not implemented"""


class Error71Dict(TypedDict):
    info: NotRequired[str]
    code: NotRequired[str]
    field: NotRequired[str]
    description: NotRequired[str]
    severity: NotRequired[str]
    category: NotRequired[str]
    http_status: NotRequired[int]
