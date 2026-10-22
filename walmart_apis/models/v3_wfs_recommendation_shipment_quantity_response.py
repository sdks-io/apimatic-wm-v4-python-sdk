from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload15 import Payload15, Payload15Dict


class V3WfsRecommendationShipmentQuantityResponse(SdkBaseModel):
    status: Optional[str] = UNSET
    payload: Optional[Payload15] = UNSET


class V3WfsRecommendationShipmentQuantityResponseDict(TypedDict):
    status: NotRequired[str]
    payload: NotRequired[Payload15Dict]
