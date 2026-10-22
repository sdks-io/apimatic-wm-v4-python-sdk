from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Error51(SdkBaseModel):
    code: Optional[str] = UNSET
    severity: Optional[str] = UNSET
    description: Optional[str] = UNSET
    category: Optional[str] = UNSET
    field: Optional[str] = UNSET


class Error51Dict(TypedDict):
    code: NotRequired[str]
    severity: NotRequired[str]
    description: NotRequired[str]
    category: NotRequired[str]
    field: NotRequired[str]
