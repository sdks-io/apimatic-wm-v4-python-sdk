from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_details2 import ItemDetails2, ItemDetails2Dict


class Record1(SdkBaseModel):
    """Information related to the item recommendations."""

    item_recommendation_unique_id: Optional[str] = Field(default=UNSET, alias="itemRecommendationUniqueId")
    """Unique identifier for the recommended item."""

    item_details: Optional[ItemDetails2] = Field(default=UNSET, alias="itemDetails")
    """Details of the recommended item."""


class Record1Dict(TypedDict):
    item_recommendation_unique_id: NotRequired[str]
    item_details: NotRequired[ItemDetails2Dict]
