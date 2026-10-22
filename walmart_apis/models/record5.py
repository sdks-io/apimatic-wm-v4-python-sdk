from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_details4 import ItemDetails4, ItemDetails4Dict


class Record5(SdkBaseModel):
    """Information related to the item recommendations."""

    item_recommendation_unique_id: Optional[str] = Field(default=UNSET, alias="itemRecommendationUniqueId")
    """Unique identifier for the recommended item. <br><b style='color:green;'>Market availability: US
    only</span></b>"""

    item_details: Optional[ItemDetails4] = Field(default=UNSET, alias="itemDetails")
    """Details of the recommended item.<br><b style='color:green;'>Market availability: US only</span></b>"""


class Record5Dict(TypedDict):
    item_recommendation_unique_id: NotRequired[str]
    item_details: NotRequired[ItemDetails4Dict]
