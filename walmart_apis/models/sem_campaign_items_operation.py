from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.operation_type import OperationTypeOrStr


class SemCampaignItemsOperation(SdkBaseModel):
    """List of operations to perform on campaign items."""

    operation_type: OperationTypeOrStr = Field(alias="operationType")
    """Type of operation to perform on campaign items. Allowed values: ``ADD`` or ``REMOVE``."""

    skus: list[str]
    """List of SKUs associated with the campaign. Must contain between 1 and 10,000 SKUs."""


class SemCampaignItemsOperationDict(TypedDict):
    operation_type: OperationTypeOrStr
    skus: list[str]
