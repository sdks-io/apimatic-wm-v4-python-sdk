from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .criteria_data2 import CriteriaData2, CriteriaData2Dict
from .meets_criteria2 import MeetsCriteria2, MeetsCriteria2Dict
from .recommendations1 import Recommendations1, Recommendations1Dict


class V3InsightsProsellerbadgeResponse(SdkBaseModel):
    has_badge: Optional[bool] = Field(default=UNSET, alias="hasBadge")
    """Specifies if the seller has the badge period.<br><b style='color:green;'>Market availability: MX only</b>"""

    is_eligible: Optional[bool] = Field(default=UNSET, alias="isEligible")
    """Specifies if the seller is eligible for the badge in the next refresh period.<br><b style='color:green;'>Market
    availability: MX only</b>"""

    badged_since: Optional[RFC3339DateTime] = Field(default=UNSET, alias="badgedSince")
    """Specifies when the seller received their badge period.<br><b style='color:green;'>Market availability: MX
    only</b>"""

    is_prohibited: Optional[bool] = Field(default=UNSET, alias="isProhibited")
    """Specifies whether the seller is prohibited from participating in the Pro Seller badge program.<br><b
    style='color:green;'>Market availability: MX only</b>"""

    badge_status: Optional[str] = Field(default=UNSET, alias="badgeStatus")
    """Specifies the seller's badge status in detail. The possible values are "Become a Pro Seller", "You are a Pro
    Seller", "Pro Seller Badge at risk", "Eligible starting from YYYY-MM-DD", and "Not eligible for the Pro Seller
    Badge"<br><b style='color:green;'>Market availability: MX only</b>"""

    meets_criteria: Optional[MeetsCriteria2] = Field(default=UNSET, alias="meetsCriteria")
    """Shows whether the seller has met the requirements for the badge.<br><b style='color:green;'>Market availability:
    MX only</b>"""

    criteria_data: Optional[CriteriaData2] = Field(default=UNSET, alias="criteriaData")
    """Shows the criteria for the Pro Seller badge.<br><b style='color:green;'>Market availability: MX only</b>"""

    recommendations: Optional[Recommendations1] = UNSET
    """Recommendations on how to increase chances of Pro Seller Badge eligibility<br><b style='color:green;'>Market
    availability: MX only</b>"""


class V3InsightsProsellerbadgeResponseDict(TypedDict):
    has_badge: NotRequired[bool]
    is_eligible: NotRequired[bool]
    badged_since: NotRequired[RFC3339DateTime]
    is_prohibited: NotRequired[bool]
    badge_status: NotRequired[str]
    meets_criteria: NotRequired[MeetsCriteria2Dict]
    criteria_data: NotRequired[CriteriaData2Dict]
    recommendations: NotRequired[Recommendations1Dict]
