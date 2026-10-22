from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Cause(SdkBaseModel):
    code: Optional[str] = UNSET
    field: Optional[str] = UNSET
    type_: Optional[str] = Field(default=UNSET, alias="type")
    description: Optional[str] = UNSET


class CauseDict(TypedDict):
    code: NotRequired[str]
    field: NotRequired[str]
    type_: NotRequired[str]
    description: NotRequired[str]
