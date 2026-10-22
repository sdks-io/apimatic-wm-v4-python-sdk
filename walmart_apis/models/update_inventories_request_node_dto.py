from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .supply_quantity import SupplyQuantity, SupplyQuantityDict


class UpdateInventoriesRequestNodeDto(SdkBaseModel):
    ship_node: str = Field(alias="shipNode")
    """ShipNode Id of the ship node for which the inventory is requested"""

    input_qty: SupplyQuantity = Field(alias="inputQty")
    """Quantity that has been ordered by the customers but not yet shipped."""

    inventory_available_date: Optional[str] = Field(default=UNSET, alias="inventoryAvailableDate")
    """Inventory available date for a ship node. Format:YYYY-MM-DD"""


class UpdateInventoriesRequestNodeDtoDict(TypedDict):
    ship_node: str
    input_qty: SupplyQuantityDict
    inventory_available_date: NotRequired[str]
