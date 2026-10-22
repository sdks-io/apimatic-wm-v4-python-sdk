from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class NonAccountableVtrDrivers(SdkBaseModel):
    """Non Accountable drivers, which impacting the valid tracking rate"""

    miscellaneous_rate: Optional[float] = Field(default=UNSET, alias="miscellaneousRate")
    """Rate of orders impacted due to miscellaneous reasons"""


class NonAccountableVtrDriversDict(TypedDict):
    miscellaneous_rate: NotRequired[float]
