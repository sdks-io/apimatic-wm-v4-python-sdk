from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SellerAccountableCancellationsDrivers(SdkBaseModel):
    """Seller accountable drivers, which impacting the cancellations rate"""

    out_of_stock_rate: Optional[float] = Field(default=UNSET, alias="outOfStockRate")
    """Rate of orders cancelled due to out of stock"""

    pricing_error_rate: Optional[float] = Field(default=UNSET, alias="pricingErrorRate")
    """Rate of orders cancelled due to pricing errors"""

    inc_mrkd_add_not_svcble_rate: Optional[float] = Field(default=UNSET, alias="incMrkdAddNotSvcbleRate")
    """Rate of orders cancelled due of incorrectly marked as address not serviceable"""

    ship_window_exp_rate: Optional[float] = Field(default=UNSET, alias="shipWindowExpRate")
    """Rate of orders cancelled due to ship window expired"""


class SellerAccountableCancellationsDriversDict(TypedDict):
    out_of_stock_rate: NotRequired[float]
    pricing_error_rate: NotRequired[float]
    inc_mrkd_add_not_svcble_rate: NotRequired[float]
    ship_window_exp_rate: NotRequired[float]
