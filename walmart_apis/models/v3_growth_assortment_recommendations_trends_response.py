from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload5 import Payload5, Payload5Dict


class V3GrowthAssortmentRecommendationsTrendsResponse(SdkBaseModel):
    payload: Optional[Payload5] = UNSET
    """Payload in the response having the trend details for the recommended item."""


class V3GrowthAssortmentRecommendationsTrendsResponseDict(TypedDict):
    payload: NotRequired[Payload5Dict]
