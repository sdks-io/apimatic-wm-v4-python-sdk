from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V3SeoRecommendationUpdateItemsResponse(SdkBaseModel):
    status: Optional[str] = UNSET
    """status of the update"""

    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    """The ID of the item that was updated."""

    message: Optional[str] = UNSET
    """Description of the response"""


class V3SeoRecommendationUpdateItemsResponseDict(TypedDict):
    status: NotRequired[str]
    item_id: NotRequired[str]
    message: NotRequired[str]
