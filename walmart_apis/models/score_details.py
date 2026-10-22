from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .content_and_discoverability import ContentAndDiscoverability, ContentAndDiscoverabilityDict
from .offer import Offer, OfferDict
from .post_purchase import PostPurchase, PostPurchaseDict
from .rating_reviews import RatingReviews, RatingReviewsDict


class ScoreDetails(SdkBaseModel):
    offer: Optional[Offer] = UNSET
    rating_reviews: Optional[RatingReviews] = Field(default=UNSET, alias="ratingReviews")
    post_purchase: Optional[PostPurchase] = Field(default=UNSET, alias="postPurchase")
    content_and_discoverability: Optional[ContentAndDiscoverability] = Field(
        default=UNSET, alias="contentAndDiscoverability"
    )


class ScoreDetailsDict(TypedDict):
    offer: NotRequired[OfferDict]
    rating_reviews: NotRequired[RatingReviewsDict]
    post_purchase: NotRequired[PostPurchaseDict]
    content_and_discoverability: NotRequired[ContentAndDiscoverabilityDict]
