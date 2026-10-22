from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Score2(SdkBaseModel):
    """Score<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    offer_score: Optional[float] = Field(default=UNSET, alias="offerScore")
    """Offer Score<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    content_score: Optional[float] = Field(default=UNSET, alias="contentScore")
    """Content Score<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    rating_review_score: Optional[float] = Field(default=UNSET, alias="ratingReviewScore")
    """Rating Review Score<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    competitive_price_score: Optional[float] = Field(default=UNSET, alias="competitivePriceScore")
    """Competitive Price Score<br><b style='color:green;'>Market availability: US</b>"""

    shipping_score: Optional[float] = Field(default=UNSET, alias="shippingScore")
    """Shipping Score<br><b style='color:green;'>Market availability: US</b>"""

    transactibility_score: Optional[float] = Field(default=UNSET, alias="transactibilityScore")
    """Rating Review Score<br><b style='color:green;'>Market availability: US</b>"""


class Score2Dict(TypedDict):
    offer_score: NotRequired[float]
    content_score: NotRequired[float]
    rating_review_score: NotRequired[float]
    competitive_price_score: NotRequired[float]
    shipping_score: NotRequired[float]
    transactibility_score: NotRequired[float]
