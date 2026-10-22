from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .post_purchase_quality import PostPurchaseQuality, PostPurchaseQualityDict
from .score import Score, ScoreDict


class ListingQualityScorePayload(SdkBaseModel):
    listing_quality: Optional[float] = Field(default=UNSET, alias="listingQuality")
    """Listing Quality"""

    score: Optional[Score] = UNSET
    """Score"""

    post_purchase_quality: Optional[PostPurchaseQuality] = Field(default=UNSET, alias="postPurchaseQuality")
    """Post Purchase Quality"""


class ListingQualityScorePayloadDict(TypedDict):
    listing_quality: NotRequired[float]
    score: NotRequired[ScoreDict]
    post_purchase_quality: NotRequired[PostPurchaseQualityDict]
