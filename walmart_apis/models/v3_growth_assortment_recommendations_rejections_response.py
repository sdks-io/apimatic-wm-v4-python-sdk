from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload7 import Payload7, Payload7Dict


class V3GrowthAssortmentRecommendationsRejectionsResponse(SdkBaseModel):
    payload: Optional[Payload7] = UNSET
    """Payload in the response for rejecting recommendations."""


class V3GrowthAssortmentRecommendationsRejectionsResponseDict(TypedDict):
    payload: NotRequired[Payload7Dict]
