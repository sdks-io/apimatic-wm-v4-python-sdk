from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money_type import MoneyType, MoneyTypeDict


class PickupDiscount(SdkBaseModel):
    is_pick_up_discount_eligible: Optional[bool] = Field(default=UNSET, alias="isPickUpDiscountEligible")
    pickup_discount_amt: Optional[MoneyType] = Field(default=UNSET, alias="pickupDiscountAmt")


class PickupDiscountDict(TypedDict):
    is_pick_up_discount_eligible: NotRequired[bool]
    pickup_discount_amt: NotRequired[MoneyTypeDict]
