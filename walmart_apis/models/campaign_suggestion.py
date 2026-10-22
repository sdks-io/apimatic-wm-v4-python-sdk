from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .campaign_recommendation import CampaignRecommendation, CampaignRecommendationDict


class CampaignSuggestion(SdkBaseModel):
    """Campaign-level suggestion containing current campaign settings and an array of actionable recommendations."""

    campaign_id: Optional[str] = Field(default=UNSET, alias="campaignId")
    """Unique campaign identifier."""

    name: Optional[str] = UNSET
    """Human-readable campaign name."""

    bidding_strategy_type: Optional[str] = Field(default=UNSET, alias="biddingStrategyType")
    """Current bidding strategy type configured for the campaign (For example, ``TARGET_ROAS``, ``MAXIMIZE_CLICKS``)."""

    target_roas: OptionalNullable[float] = Field(default=UNSET, alias="targetRoas")
    """Current target Return on Ad Spend (ROAS) configured for the campaign. Only applicable when
    ``biddingStrategyType`` is ``TARGET_ROAS``."""

    daily_budget: Optional[float] = Field(default=UNSET, alias="dailyBudget")
    """Current daily budget configured for the campaign (in USD)."""

    campaign_recommendations: Optional[list[CampaignRecommendation]] = Field(
        default=UNSET, alias="campaignRecommendations"
    )
    """List of actionable recommendations for this campaign. Each recommendation includes the type, recommended value,
    and projected performance impact."""


class CampaignSuggestionDict(TypedDict):
    campaign_id: NotRequired[str]
    name: NotRequired[str]
    bidding_strategy_type: NotRequired[str]
    target_roas: NotRequired[float | None]
    daily_budget: NotRequired[float]
    campaign_recommendations: NotRequired[list[CampaignRecommendationDict]]
