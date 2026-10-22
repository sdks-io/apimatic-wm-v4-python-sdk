from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .lag_time1 import LagTime1, LagTime1Dict
from .lag_time_header import LagTimeHeader, LagTimeHeaderDict


class LagTimeFeed(SdkBaseModel):
    lag_time_header: LagTimeHeader = Field(alias="lagTimeHeader")
    lag_time: Optional[list[LagTime1]] = Field(default=UNSET, alias="lagTime")


class LagTimeFeedDict(TypedDict):
    lag_time_header: LagTimeHeaderDict
    lag_time: NotRequired[list[LagTime1Dict]]
