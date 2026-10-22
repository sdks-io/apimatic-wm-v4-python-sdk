from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload4 import Payload4, Payload4Dict


class V3GrowthAssortmentRecommendationsVariantsResponse(SdkBaseModel):
    payload: Optional[Payload4] = UNSET
    """Payload in the response having the details about the item recommendations."""


class V3GrowthAssortmentRecommendationsVariantsResponseDict(TypedDict):
    payload: NotRequired[Payload4Dict]
