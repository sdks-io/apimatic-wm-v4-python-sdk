from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TotalInsight2(SdkBaseModel):
    total_unpublished_units_stored: Optional[float] = Field(default=UNSET, alias="totalUnpublishedUnitsStored")
    """The total number of units of all your unpublished items that are currently in stock at WFS fulfillment
    centers."""

    total_estimated_storage_fee: Optional[float] = Field(default=UNSET, alias="totalEstimatedStorageFee")
    """Based on your current inventory level, this is the estimated total cost of storing your unpublished WFS items for
    the next 30 days."""

    total_inventory_value: Optional[float] = Field(default=UNSET, alias="totalInventoryValue")
    """The estimated total dollar value of the available inventory for all your WFS unpublished items."""


class TotalInsight2Dict(TypedDict):
    total_unpublished_units_stored: NotRequired[float]
    total_estimated_storage_fee: NotRequired[float]
    total_inventory_value: NotRequired[float]
