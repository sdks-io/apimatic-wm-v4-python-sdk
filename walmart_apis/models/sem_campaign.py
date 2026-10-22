from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SemCampaign(SdkBaseModel):
    campaign_id: Optional[str] = Field(default=UNSET, alias="campaignId")
    """Unique identifier for the campaign."""

    name: Optional[str] = UNSET
    """Name of the campaign."""

    start_date: Optional[str] = Field(default=UNSET, alias="startDate")
    """Start date of the campaign in 'YYYY-MM-DD' format."""

    end_date: Optional[str] = Field(default=UNSET, alias="endDate")
    """End date of the campaign in 'YYYY-MM-DD' format."""

    daily_budget: Optional[float] = Field(default=UNSET, alias="dailyBudget")
    """Daily budget allocated for the campaign."""

    total_budget: Optional[float] = Field(default=UNSET, alias="totalBudget")
    """Total budget allocated for the campaign."""

    bidding_strategy_type: Optional[str] = Field(default=UNSET, alias="biddingStrategyType")
    """Bidding strategy type for the campaign."""

    target_roas: Optional[float] = Field(default=UNSET, alias="targetRoas")
    """Target ROAS for the campaign."""

    status: Optional[str] = UNSET
    """Current status of the campaign."""

    created_date: Optional[str] = Field(default=UNSET, alias="createdDate")
    """Date when the campaign was created in 'YYYY-MM-DD' format."""


class SemCampaignDict(TypedDict):
    campaign_id: NotRequired[str]
    name: NotRequired[str]
    start_date: NotRequired[str]
    end_date: NotRequired[str]
    daily_budget: NotRequired[float]
    total_budget: NotRequired[float]
    bidding_strategy_type: NotRequired[str]
    target_roas: NotRequired[float]
    status: NotRequired[str]
    created_date: NotRequired[str]
