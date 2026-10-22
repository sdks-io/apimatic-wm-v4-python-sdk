from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Insight2(SdkBaseModel):
    unpublished_issue_type: Optional[str] = Field(default=UNSET, alias="unpublishedIssueType")
    """High-level issue type explaining why your item is unpublished."""

    estimated_storage_fee: Optional[float] = Field(default=UNSET, alias="estimatedStorageFee")
    """Based on your current inventory level, this is the estimated per-unit storage cost of your unpublished WFS items
    for the next 30 days."""

    inventory_value: Optional[float] = Field(default=UNSET, alias="inventoryValue")
    """The estimated dollar value of the available inventory for each unpublished WFS item in your catalog."""

    customer_favorite: Optional[bool] = Field(default=UNSET, alias="customerFavorite")
    """Indicates whether the item is identified as a customer favorite based on customer demand."""


class Insight2Dict(TypedDict):
    unpublished_issue_type: NotRequired[str]
    estimated_storage_fee: NotRequired[float]
    inventory_value: NotRequired[float]
    customer_favorite: NotRequired[bool]
