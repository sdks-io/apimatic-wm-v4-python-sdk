from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .post_purchase_quality2 import PostPurchaseQuality2, PostPurchaseQuality2Dict
from .score2 import Score2, Score2Dict


class Payload17(SdkBaseModel):
    listing_quality: Optional[float] = Field(default=UNSET, alias="listingQuality")
    """Indicates the Listing Quality Score of a product listing.<br><b style='color:green;'>Market availability: US | CA
    | MX</b>"""

    score: Optional[Score2] = UNSET
    """Score<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    post_purchase_quality: Optional[PostPurchaseQuality2] = Field(default=UNSET, alias="postPurchaseQuality")
    """Post Purchase Quality<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class Payload17Dict(TypedDict):
    listing_quality: NotRequired[float]
    score: NotRequired[Score2Dict]
    post_purchase_quality: NotRequired[PostPurchaseQuality2Dict]
