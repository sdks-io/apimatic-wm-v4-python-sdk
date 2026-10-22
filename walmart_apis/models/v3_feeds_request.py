from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .lag_time2 import LagTime2, LagTime2Dict
from .lag_time_header1 import LagTimeHeader1, LagTimeHeader1Dict


class V3FeedsRequest(SdkBaseModel):
    lag_time_header: LagTimeHeader1 = Field(alias="lagTimeHeader")
    """Defines the header metadata for a lag time update feed.

    <strong style="color: green;">Market availability: Global</strong>"""

    lag_time: Optional[list[LagTime2]] = Field(default=UNSET, alias="lagTime")
    """Details for each lag time entry.

    <strong style="color: green;">Market availability: Global</strong>"""


class V3FeedsRequestDict(TypedDict):
    lag_time_header: LagTimeHeader1Dict
    lag_time: NotRequired[list[LagTime2Dict]]
