from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload110 import Payload110, Payload110Dict


class V3WfsRecommendationRestockResponse(SdkBaseModel):
    status: Optional[str] = UNSET
    payload: Optional[Payload110] = UNSET


class V3WfsRecommendationRestockResponseDict(TypedDict):
    status: NotRequired[str]
    payload: NotRequired[Payload110Dict]
