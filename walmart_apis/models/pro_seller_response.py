from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .criteria_data import CriteriaData, CriteriaDataDict
from .meets_criteria import MeetsCriteria, MeetsCriteriaDict
from .recommendations import Recommendations, RecommendationsDict


class ProSellerResponse(SdkBaseModel):
    has_badge: Optional[bool] = Field(default=UNSET, alias="hasBadge")
    """Specifies if the seller has the badge"""

    is_eligible: Optional[bool] = Field(default=UNSET, alias="isEligible")
    """Specifies if the seller is eligible for the badge in the next refresh"""

    badged_since: Optional[RFC3339DateTime] = Field(default=UNSET, alias="badgedSince")
    """Specifies when the seller received their badge"""

    is_prohibited: Optional[bool] = Field(default=UNSET, alias="isProhibited")
    """Specifies whether the seller is prohibited from participating in the Pro Seller badge program."""

    badge_status: Optional[str] = Field(default=UNSET, alias="badgeStatus")
    """Specifies the seller's badge status in detail. The possible values are "Become a Pro Seller", "You are a Pro
    Seller", "Pro Seller Badge at risk", "Eligible starting from YYYY-MM-DD", and "Not eligible for the Pro Seller
    Badge"
    """

    meets_criteria: Optional[MeetsCriteria] = Field(default=UNSET, alias="meetsCriteria")
    """Shows whether the seller has met the requirements for the badge."""

    criteria_data: Optional[CriteriaData] = Field(default=UNSET, alias="criteriaData")
    """Shows the criteria for the Pro Seller badge."""

    recommendations: Optional[Recommendations] = UNSET
    """Recommendations on how to increase chances of Pro Seller Badge eligibility"""


class ProSellerResponseDict(TypedDict):
    has_badge: NotRequired[bool]
    is_eligible: NotRequired[bool]
    badged_since: NotRequired[RFC3339DateTime]
    is_prohibited: NotRequired[bool]
    badge_status: NotRequired[str]
    meets_criteria: NotRequired[MeetsCriteriaDict]
    criteria_data: NotRequired[CriteriaDataDict]
    recommendations: NotRequired[RecommendationsDict]
