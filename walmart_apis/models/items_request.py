from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ItemsRequest(SdkBaseModel):
    """Items"""

    item_id: str = Field(alias="itemId")
    """Specifies the item identifier."""

    target_reviews: Optional[int] = Field(default=UNSET, alias="targetReviews")
    """Custom target number of reviews requested to be collected for the item. Default is 5."""


class ItemsRequestDict(TypedDict):
    item_id: str
    target_reviews: NotRequired[int]
