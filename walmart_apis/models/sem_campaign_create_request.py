from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .sem_campaign_create_metadata import SemCampaignCreateMetadata, SemCampaignCreateMetadataDict
from .sem_campaign_items_operation import SemCampaignItemsOperation, SemCampaignItemsOperationDict


class SemCampaignCreateRequest(SdkBaseModel):
    metadata: SemCampaignCreateMetadata
    """Metadata for creating a campaign."""

    items_operations: list[SemCampaignItemsOperation] = Field(alias="itemsOperations")
    """List of operations to perform on campaign items."""


class SemCampaignCreateRequestDict(TypedDict):
    metadata: SemCampaignCreateMetadataDict
    items_operations: list[SemCampaignItemsOperationDict]
