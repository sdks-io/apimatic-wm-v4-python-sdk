from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V3InsightsItemsListingQualityScore500Error(SdkBaseModel):
    timestamp: Optional[str] = UNSET
    status: Optional[float] = UNSET
    error: Optional[str] = UNSET
    path: Optional[str] = UNSET


class V3InsightsItemsListingQualityScore500ErrorDict(TypedDict):
    timestamp: NotRequired[str]
    status: NotRequired[float]
    error: NotRequired[str]
    path: NotRequired[str]
