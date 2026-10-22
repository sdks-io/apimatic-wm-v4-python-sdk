from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .listing_quality_score_payload import ListingQualityScorePayload, ListingQualityScorePayloadDict


class GetListingQualityScore(SdkBaseModel):
    payload: Optional[ListingQualityScorePayload] = UNSET


class GetListingQualityScoreDict(TypedDict):
    payload: NotRequired[ListingQualityScorePayloadDict]
