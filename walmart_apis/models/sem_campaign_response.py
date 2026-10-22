from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SemCampaignResponse(SdkBaseModel):
    campaign_id: Optional[str] = Field(default=UNSET, alias="campaignId")
    """Unique identifier for the campaign."""


class SemCampaignResponseDict(TypedDict):
    campaign_id: NotRequired[str]
