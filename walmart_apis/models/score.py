from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Score(SdkBaseModel):
    """Score"""

    offer_score: Optional[float] = Field(default=UNSET, alias="offerScore")
    """Offer Score"""

    content_score: Optional[float] = Field(default=UNSET, alias="contentScore")
    """Content Score"""

    rating_review_score: Optional[float] = Field(default=UNSET, alias="ratingReviewScore")
    """Rating Review Score"""


class ScoreDict(TypedDict):
    offer_score: NotRequired[float]
    content_score: NotRequired[float]
    rating_review_score: NotRequired[float]
