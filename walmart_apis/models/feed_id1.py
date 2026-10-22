from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FeedId1(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>, Response returned upon successful feed
    submission."""

    feed_id: Optional[str] = Field(default=UNSET, alias="feedId")
    """A unique ID, returned from the Bulk Upload API, used for tracking the Feed File."""


class FeedId1Dict(TypedDict):
    feed_id: NotRequired[str]
