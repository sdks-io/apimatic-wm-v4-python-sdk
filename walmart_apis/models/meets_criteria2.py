from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MeetsCriteria2(SdkBaseModel):
    """Shows whether the seller has met the requirements for the badge.<br><b style='color:green;'>Market availability:
    MX only</b>"""

    orders_criteria_met: Optional[bool] = Field(default=UNSET, alias="ordersCriteriaMet")
    """Indicates whether the seller has met the minimum number of orders required.<br><b style='color:green;'>Market
    availability: MX only</b>"""

    delivery_defect_criteria_met: Optional[bool] = Field(default=UNSET, alias="deliveryDefectCriteriaMet")
    """Indicates whether the seller has a low delivery defect, meeting the threshold for the badge.<br><b
    style='color:green;'>Market availability: MX only</b>"""

    cancellation_criteria_met: Optional[bool] = Field(default=UNSET, alias="cancellationCriteriaMet")
    """Indicates whether the seller has a low cancellation rate, meeting the threshold for the badge.<br><b
    style='color:green;'>Market availability: MX only</b>"""

    actual_vs_promised_gap_criteria_met: Optional[bool] = Field(default=UNSET, alias="actualVsPromisedGapCriteriaMet")
    """Indicates whether the seller has a low gap between actual and promised delivery dates, meeting the threshold for
    the badge.<br><b style='color:green;'>Market availability: MX only</b>"""

    active_days_criteria_met: Optional[bool] = Field(default=UNSET, alias="activeDaysCriteriaMet")
    """Indicates whether the seller has met the minimum number of active days required.<br><b
    style='color:green;'>Market availability: MX only</b>"""


class MeetsCriteria2Dict(TypedDict):
    orders_criteria_met: NotRequired[bool]
    delivery_defect_criteria_met: NotRequired[bool]
    cancellation_criteria_met: NotRequired[bool]
    actual_vs_promised_gap_criteria_met: NotRequired[bool]
    active_days_criteria_met: NotRequired[bool]
