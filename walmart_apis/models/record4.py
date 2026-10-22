from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_details3 import ItemDetails3, ItemDetails3Dict


class Record4(SdkBaseModel):
    """Information related to the item recommendations."""

    item_recommendation_unique_id: Optional[str] = Field(default=UNSET, alias="itemRecommendationUniqueId")
    """Unique identifier for the recommended item. <br><b style='color:green;'>Market availability: US | CA |
    MX</span></b>"""

    item_details: Optional[ItemDetails3] = Field(default=UNSET, alias="itemDetails")
    """Details of the recommended item."""


class Record4Dict(TypedDict):
    item_recommendation_unique_id: NotRequired[str]
    item_details: NotRequired[ItemDetails3Dict]
