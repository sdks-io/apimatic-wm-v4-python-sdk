from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ContentDiscoverabilityIssuesDesc(SdkBaseModel):
    title: Optional[str] = UNSET
    value: Optional[str] = UNSET


class ContentDiscoverabilityIssuesDescDict(TypedDict):
    title: NotRequired[str]
    value: NotRequired[str]
