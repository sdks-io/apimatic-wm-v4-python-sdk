from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CampaignRef(SdkBaseModel):
    """Campaign association reference. Represents a campaign that an item belongs to. A single item can appear in
    multiple campaigns."""

    campaign_id: Optional[str] = Field(default=UNSET, alias="campaignId")
    """Campaign identifier."""

    campaign_name: Optional[str] = Field(default=UNSET, alias="campaignName")
    """Human-readable campaign name."""


class CampaignRefDict(TypedDict):
    campaign_id: NotRequired[str]
    campaign_name: NotRequired[str]
