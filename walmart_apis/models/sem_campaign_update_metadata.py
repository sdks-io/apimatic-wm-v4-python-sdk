from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.bidding_strategy_type import BiddingStrategyTypeOrStr


class SemCampaignUpdateMetadata(SdkBaseModel):
    """Metadata for updating the campaign."""

    name: Optional[str] = UNSET
    """Name of the campaign. Allowed characters: letters, digits, dashes, underscores, and spaces. Maximum 255
    characters allowed."""

    start_date: Optional[str] = Field(default=UNSET, alias="startDate")
    """Start date of the campaign in YYYY-MM-DD format."""

    end_date: str = Field(default="", alias="endDate")
    """End date of the campaign in YYYY-MM-DD format."""

    daily_budget: Optional[float] = Field(default=UNSET, alias="dailyBudget")
    """Daily budget allocated for the campaign. Must be a positive value with up to two decimal places. Daily budget
    must be between $5.00 and $2,500.00."""

    total_budget: Optional[float] = Field(default=UNSET, alias="totalBudget")
    """Total budget allocated for the campaign. Total budget must be between $5.00 and $250,000.00. Cannot be updated to
    a value less than what has already been spent."""

    bidding_strategy_type: Optional[BiddingStrategyTypeOrStr] = Field(default=UNSET, alias="biddingStrategyType")
    """Bidding strategy type for the campaign."""

    target_roas: float = Field(default=3.5, alias="targetRoas")
    """Target ROAS for the campaign. Must be a positive value, with up to two decimal places."""


class SemCampaignUpdateMetadataDict(TypedDict):
    name: NotRequired[str]
    start_date: NotRequired[str]
    end_date: NotRequired[str]
    daily_budget: NotRequired[float]
    total_budget: NotRequired[float]
    bidding_strategy_type: NotRequired[BiddingStrategyTypeOrStr]
    target_roas: NotRequired[float]
