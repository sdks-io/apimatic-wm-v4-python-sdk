from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .gmv import Gmv, GmvDict


class Stats(SdkBaseModel):
    gmv: Optional[Gmv] = UNSET
    page_views: Optional[str] = Field(default=UNSET, alias="pageViews")
    orders: Optional[str] = UNSET
    conversion_rate: Optional[str] = Field(default=UNSET, alias="conversionRate")
    total_units: Optional[str] = Field(default=UNSET, alias="totalUnits")


class StatsDict(TypedDict):
    gmv: NotRequired[GmvDict]
    page_views: NotRequired[str]
    orders: NotRequired[str]
    conversion_rate: NotRequired[str]
    total_units: NotRequired[str]
