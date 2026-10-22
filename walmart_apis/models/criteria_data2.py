from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CriteriaData2(SdkBaseModel):
    """Shows the criteria for the Pro Seller badge.<br><b style='color:green;'>Market availability: MX only</b>"""

    orders: Optional[int] = UNSET
    """Number of orders received during the last 90 days.<br><b style='color:green;'>Market availability: MX only</b>"""

    delivery_defect_rate: Optional[str] = Field(default=UNSET, alias="deliveryDefectRate")
    """Delivery Defect rate in the given timeframe.<br><b style='color:green;'>Market availability: MX only</b>"""

    cancellation_rate: Optional[str] = Field(default=UNSET, alias="cancellationRate")
    """Cancellation rate in the given timeframe.<br><b style='color:green;'>Market availability: MX only</b>"""

    actual_vs_promised_gap: Optional[int] = Field(default=UNSET, alias="actualVsPromisedGap")
    """Avg gap (in days) between actual and promised delivery in the given timeframe.<br><b style='color:green;'>Market
    availability: MX only</b>"""

    active_days: Optional[int] = Field(default=UNSET, alias="activeDays")
    """Days active on the platform.<br><b style='color:green;'>Market availability: MX only</b>"""


class CriteriaData2Dict(TypedDict):
    orders: NotRequired[int]
    delivery_defect_rate: NotRequired[str]
    cancellation_rate: NotRequired[str]
    actual_vs_promised_gap: NotRequired[int]
    active_days: NotRequired[int]
