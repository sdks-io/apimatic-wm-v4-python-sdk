from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload22 import Payload22, Payload22Dict


class V3WfsRecommendationFulfilWithWfsResponse(SdkBaseModel):
    status: Optional[str] = UNSET
    payload: Optional[Payload22] = UNSET


class V3WfsRecommendationFulfilWithWfsResponseDict(TypedDict):
    status: NotRequired[str]
    payload: NotRequired[Payload22Dict]
