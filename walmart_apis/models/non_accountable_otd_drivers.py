from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class NonAccountableOtdDrivers(SdkBaseModel):
    """Non Accountable drivers, which impacting the on time delivery rate"""

    carrier_delays_rate: Optional[float] = Field(default=UNSET, alias="carrierDelaysRate")
    """Rate of orders impacted due to carrier delays"""

    carrier_exception_rate: Optional[float] = Field(default=UNSET, alias="carrierExceptionRate")
    """Rate of orders impacted due to carrier exceptions"""

    miscellaneous_rate: Optional[float] = Field(default=UNSET, alias="miscellaneousRate")
    """Rate of orders impacted due to miscellaneous reasons"""


class NonAccountableOtdDriversDict(TypedDict):
    carrier_delays_rate: NotRequired[float]
    carrier_exception_rate: NotRequired[float]
    miscellaneous_rate: NotRequired[float]
