from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pickup_discount_amt5 import PickupDiscountAmt5, PickupDiscountAmt5Dict


class PickupDiscount1(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: Global</b>"""

    is_pick_up_discount_eligible: Optional[bool] = Field(default=UNSET, alias="isPickUpDiscountEligible")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    pickup_discount_amt: Optional[PickupDiscountAmt5] = Field(default=UNSET, alias="pickupDiscountAmt")
    """<br><b style='color:green;'>Market availability: Global</b>"""


class PickupDiscount1Dict(TypedDict):
    is_pick_up_discount_eligible: NotRequired[bool]
    pickup_discount_amt: NotRequired[PickupDiscountAmt5Dict]
