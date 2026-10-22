from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type2 import Type2OrStr


class IngestionError(SdkBaseModel):
    type_: Type2OrStr = Field(alias="type")
    """Indicates the error type."""

    code: str
    """Specifies the error code."""

    description: Optional[str] = UNSET
    """Error description"""


class IngestionErrorDict(TypedDict):
    type_: Type2OrStr
    code: str
    description: NotRequired[str]
