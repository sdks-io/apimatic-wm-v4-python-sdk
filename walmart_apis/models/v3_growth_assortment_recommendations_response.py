from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload3 import Payload3, Payload3Dict


class V3GrowthAssortmentRecommendationsResponse(SdkBaseModel):
    payload: Optional[Payload3] = UNSET
    """Payload in the response having the details about the item recommendations."""


class V3GrowthAssortmentRecommendationsResponseDict(TypedDict):
    payload: NotRequired[Payload3Dict]
