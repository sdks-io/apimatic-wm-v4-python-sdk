from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SellerAccountableRefundsDrivers(SdkBaseModel):
    """Seller accountable drivers, which impacting the refunds rate"""

    incorrect_items_rate: Optional[float] = Field(default=UNSET, alias="incorrectItemsRate")
    """Refund rate of incorrect items delivered"""

    arrived_late_rate: Optional[float] = Field(default=UNSET, alias="arrivedLateRate")
    """Refund rate of delivered late orders"""

    defective_rate: Optional[float] = Field(default=UNSET, alias="defectiveRate")
    """Refund rate of defective orders"""

    damaged_rate: Optional[float] = Field(default=UNSET, alias="damagedRate")
    """Refund rate of damaged orders"""

    lost_rate: Optional[float] = Field(default=UNSET, alias="lostRate")
    """Refund rate of lost orders"""


class SellerAccountableRefundsDriversDict(TypedDict):
    incorrect_items_rate: NotRequired[float]
    arrived_late_rate: NotRequired[float]
    defective_rate: NotRequired[float]
    damaged_rate: NotRequired[float]
    lost_rate: NotRequired[float]
