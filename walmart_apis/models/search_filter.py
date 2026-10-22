from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.field7 import Field7OrStr


class SearchFilter(SdkBaseModel):
    fields: Optional[list[Field7OrStr]] = UNSET
    text: Optional[str] = UNSET


class SearchFilterDict(TypedDict):
    fields: NotRequired[list[Field7OrStr]]
    text: NotRequired[str]
