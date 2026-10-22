from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .supply_quantity import SupplyQuantity, SupplyQuantityDict


class V3Inventory400Error(SdkBaseModel):
    sku: str
    """A seller-provided Product ID. Response will have decoded value."""

    quantity: SupplyQuantity
    """Quantity that has been ordered by the customers but not yet shipped."""

    inventory_available_date: Optional[str] = Field(default=UNSET, alias="inventoryAvailableDate")
    """Information about when the inventory is expected at the given ship node.Format:YYYY-MM-DD"""


class V3Inventory400ErrorDict(TypedDict):
    sku: str
    quantity: SupplyQuantityDict
    inventory_available_date: NotRequired[str]
