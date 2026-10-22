from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload31 import Payload31, Payload31Dict


class V3WfsRecommendationUnpublishedResponse(SdkBaseModel):
    status: Optional[str] = UNSET
    payload: Optional[Payload31] = UNSET


class V3WfsRecommendationUnpublishedResponseDict(TypedDict):
    status: NotRequired[str]
    payload: NotRequired[Payload31Dict]
