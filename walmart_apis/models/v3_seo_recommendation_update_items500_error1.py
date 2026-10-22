from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V3SeoRecommendationUpdateItems500Error1(SdkBaseModel):
    status: Optional[str] = UNSET
    """status of the update"""

    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    """The ID of the item that was updated."""

    message: Optional[str] = UNSET
    """Description of the response"""

    error: Optional[str] = UNSET
    """Description of what went wrong"""


class V3SeoRecommendationUpdateItems500Error1Dict(TypedDict):
    status: NotRequired[str]
    item_id: NotRequired[str]
    message: NotRequired[str]
    error: NotRequired[str]
