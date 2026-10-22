from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class NotFoundResponse(SdkBaseModel):
    timestamp: Optional[RFC3339DateTime] = UNSET
    status: Optional[int] = UNSET
    error: Optional[str] = UNSET
    path: Optional[str] = UNSET


class NotFoundResponseDict(TypedDict):
    timestamp: NotRequired[RFC3339DateTime]
    status: NotRequired[int]
    error: NotRequired[str]
    path: NotRequired[str]
