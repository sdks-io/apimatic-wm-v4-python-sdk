from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload6 import Payload6, Payload6Dict


class V3GrowthAssortmentRecommendationsCategorizationCountsResponse(SdkBaseModel):
    payload: Optional[Payload6] = UNSET
    """Payload in the response having the categorization details about the item recommendations."""


class V3GrowthAssortmentRecommendationsCategorizationCountsResponseDict(TypedDict):
    payload: NotRequired[Payload6Dict]
