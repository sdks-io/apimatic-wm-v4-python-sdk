from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .criteria_metadata import CriteriaMetadata, CriteriaMetadataDict
from .criteria_tier import CriteriaTier, CriteriaTierDict
from .reward import Reward, RewardDict


class V3InsightsSellerIncentivesResponse(SdkBaseModel):
    partner_id: Optional[str] = Field(default=UNSET, alias="partnerId")
    """Specifies a unique ID assigned to the partner.<br><b style='color:green;'>Market availability: US | CA</b>"""

    current_tier: Optional[str] = Field(default=UNSET, alias="currentTier")
    """Specifies the current tier of the seller on the Marketplace platform.<br><b style='color:green;'>Market
    availability: US | CA</b>"""

    eligible_tier: Optional[str] = Field(default=UNSET, alias="eligibleTier")
    """Specifies the next eligible tier for the seller on the Marketplace platform.<br><b style='color:green;'>Market
    availability: US | CA</b>"""

    pro_seller_badge_enrolled_date: Optional[str] = Field(default=UNSET, alias="proSellerBadgeEnrolledDate")
    """Specifies the date when the seller received their badge.<br><b style='color:green;'>Market availability: US |
    CA</b>"""

    criteria_metadata: Optional[CriteriaMetadata] = Field(default=UNSET, alias="criteriaMetadata")
    """Specifies the metadata value for each criterion<br><b style='color:green;'>Market availability: US only</b>"""

    criteria_tier: Optional[CriteriaTier] = Field(default=UNSET, alias="criteriaTier")
    """Specifies the tier for each criterion.<br><b style='color:green;'>Market availability: US | CA</b>"""

    is_tier_override: Optional[bool] = Field(default=UNSET, alias="isTierOverride")
    """Indicates if the tier has been overridden.<br><b style='color:green;'>Market availability: US | CA</b>"""

    tier_override: Optional[str] = Field(default=UNSET, alias="tierOverride")
    """Specifies the overridden tier.<br><b style='color:green;'>Market availability: US | CA</b>"""

    reason_codes: Optional[list[str]] = Field(default=UNSET, alias="reasonCodes")
    """Specifies the reason codes for tier ineligibility.<br><b style='color:green;'>Market availability: US | CA</b>"""

    next_refresh_date: Optional[str] = Field(default=UNSET, alias="nextRefreshDate")
    """Specifies the date of next tier refresh.<br><b style='color:green;'>Market availability: US | CA</b>"""

    rewards: Optional[list[Reward]] = UNSET
    """Specifies the list of rewards.<br><b style='color:green;'>Market availability: US | CA</b>"""


class V3InsightsSellerIncentivesResponseDict(TypedDict):
    partner_id: NotRequired[str]
    current_tier: NotRequired[str]
    eligible_tier: NotRequired[str]
    pro_seller_badge_enrolled_date: NotRequired[str]
    criteria_metadata: NotRequired[CriteriaMetadataDict]
    criteria_tier: NotRequired[CriteriaTierDict]
    is_tier_override: NotRequired[bool]
    tier_override: NotRequired[str]
    reason_codes: NotRequired[list[str]]
    next_refresh_date: NotRequired[str]
    rewards: NotRequired[list[RewardDict]]
