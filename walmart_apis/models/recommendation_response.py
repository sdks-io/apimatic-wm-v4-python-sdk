from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload1 import Payload1, Payload1Dict


class RecommendationResponse(SdkBaseModel):
    payload: Optional[Payload1] = UNSET
    """Payload in the response having the details about the item recommendations."""


class RecommendationResponseDict(TypedDict):
    payload: NotRequired[Payload1Dict]
