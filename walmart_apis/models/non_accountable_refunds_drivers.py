from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class NonAccountableRefundsDrivers(SdkBaseModel):
    """Non Accountable drivers, which impacting the refunds rate"""

    customer_changed_mind_rate: Optional[float] = Field(default=UNSET, alias="customerChangedMindRate")
    """Refund rate of returns due to customer changed mind"""

    miscellaneous_rate: Optional[float] = Field(default=UNSET, alias="miscellaneousRate")
    """Refund rate of returns due to miscellaneous reasons"""

    undelivered_rate: Optional[float] = Field(default=UNSET, alias="undeliveredRate")
    """Refund rate of undelivered orders"""


class NonAccountableRefundsDriversDict(TypedDict):
    customer_changed_mind_rate: NotRequired[float]
    miscellaneous_rate: NotRequired[float]
    undelivered_rate: NotRequired[float]
