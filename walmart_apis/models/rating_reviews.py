from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RatingReviews(SdkBaseModel):
    max_rating: Optional[str] = Field(default=UNSET, alias="maxRating")
    rating_count: Optional[str] = Field(default=UNSET, alias="ratingCount")


class RatingReviewsDict(TypedDict):
    max_rating: NotRequired[str]
    rating_count: NotRequired[str]
