from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LagTimeHeader(SdkBaseModel):
    version: Optional[str] = UNSET
    feed_date: Optional[str] = Field(default=UNSET, alias="feedDate")


class LagTimeHeaderDict(TypedDict):
    version: NotRequired[str]
    feed_date: NotRequired[str]
