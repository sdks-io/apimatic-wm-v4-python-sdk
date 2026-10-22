from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LagTimeHeader1(SdkBaseModel):
    """Defines the header metadata for a lag time update feed.

    <strong style="color: green;">Market availability: Global</strong>"""

    version: Optional[str] = UNSET
    feed_date: Optional[str] = Field(default=UNSET, alias="feedDate")


class LagTimeHeader1Dict(TypedDict):
    version: NotRequired[str]
    feed_date: NotRequired[str]
