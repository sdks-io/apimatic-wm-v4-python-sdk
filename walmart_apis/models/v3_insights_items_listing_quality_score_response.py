from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload17 import Payload17, Payload17Dict


class V3InsightsItemsListingQualityScoreResponse(SdkBaseModel):
    payload: Optional[Payload17] = UNSET


class V3InsightsItemsListingQualityScoreResponseDict(TypedDict):
    payload: NotRequired[Payload17Dict]
