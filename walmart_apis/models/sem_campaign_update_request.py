from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sem_campaign_items_operation import SemCampaignItemsOperation, SemCampaignItemsOperationDict
from .sem_campaign_update_metadata import SemCampaignUpdateMetadata, SemCampaignUpdateMetadataDict


class SemCampaignUpdateRequest(SdkBaseModel):
    metadata: Optional[SemCampaignUpdateMetadata] = UNSET
    """Metadata for updating the campaign."""

    items_operations: Optional[list[SemCampaignItemsOperation]] = Field(default=UNSET, alias="itemsOperations")
    """List of operations to perform on campaign items."""


class SemCampaignUpdateRequestDict(TypedDict):
    metadata: NotRequired[SemCampaignUpdateMetadataDict]
    items_operations: NotRequired[list[SemCampaignItemsOperationDict]]
