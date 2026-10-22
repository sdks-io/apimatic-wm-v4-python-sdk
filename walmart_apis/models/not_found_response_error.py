from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class NotFoundResponseError(SdkBaseModel):
    timestamp: Optional[RFC3339DateTime] = UNSET
    status: Optional[int] = UNSET
    error: Optional[str] = UNSET
    path: Optional[str] = UNSET


class NotFoundResponseErrorDict(TypedDict):
    timestamp: NotRequired[RFC3339DateTime]
    status: NotRequired[int]
    error: NotRequired[str]
    path: NotRequired[str]
