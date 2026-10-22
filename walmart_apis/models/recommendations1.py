from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Recommendations1(SdkBaseModel):
    """Recommendations on how to increase chances of Pro Seller Badge eligibility<br><b style='color:green;'>Market
    availability: MX only</b>"""

    delivery_defect_rate: Optional[str] = Field(default=UNSET, alias="deliveryDefectRate")
    """Recommendations on reducing the delivery defect rate<br><b style='color:green;'>Market availability: MX
    only</b>"""

    cancellation_rate: Optional[str] = Field(default=UNSET, alias="cancellationRate")
    """Recommendations on reducing the Cancellation rate<br><b style='color:green;'>Market availability: MX only</b>"""

    actual_vs_promised_gap: Optional[str] = Field(default=UNSET, alias="actualVsPromisedGap")
    """Recommendations on reducing the Actual vs Promised Delivery Gap<br><b style='color:green;'>Market availability:
    MX only</b>"""


class Recommendations1Dict(TypedDict):
    delivery_defect_rate: NotRequired[str]
    cancellation_rate: NotRequired[str]
    actual_vs_promised_gap: NotRequired[str]
