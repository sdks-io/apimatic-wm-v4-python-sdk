from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RatingReviews2(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    max_rating: Optional[str] = Field(default=UNSET, alias="maxRating")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    rating_count: Optional[str] = Field(default=UNSET, alias="ratingCount")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class RatingReviews2Dict(TypedDict):
    max_rating: NotRequired[str]
    rating_count: NotRequired[str]
