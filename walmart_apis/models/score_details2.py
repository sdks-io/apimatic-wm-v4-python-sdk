from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .content_and_discoverability4 import ContentAndDiscoverability4, ContentAndDiscoverability4Dict
from .offer2 import Offer2, Offer2Dict
from .post_purchase2 import PostPurchase2, PostPurchase2Dict
from .rating_reviews2 import RatingReviews2, RatingReviews2Dict


class ScoreDetails2(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    offer: Optional[Offer2] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    rating_reviews: Optional[RatingReviews2] = Field(default=UNSET, alias="ratingReviews")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    post_purchase: Optional[PostPurchase2] = Field(default=UNSET, alias="postPurchase")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    content_and_discoverability: Optional[ContentAndDiscoverability4] = Field(
        default=UNSET, alias="contentAndDiscoverability"
    )
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class ScoreDetails2Dict(TypedDict):
    offer: NotRequired[Offer2Dict]
    rating_reviews: NotRequired[RatingReviews2Dict]
    post_purchase: NotRequired[PostPurchase2Dict]
    content_and_discoverability: NotRequired[ContentAndDiscoverability4Dict]
