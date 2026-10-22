from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .avail_to_sell_qty import AvailToSellQty, AvailToSellQtyDict
from .input_qty import InputQty, InputQtyDict
from .supply_quantity import SupplyQuantity, SupplyQuantityDict


class GetAllInventoriesNodeDto(SdkBaseModel):
    ship_node: Optional[str] = Field(default=UNSET, alias="shipNode")
    """ShipNode Id of the ship node for which the inventory is requested"""

    input_qty: Optional[InputQty] = Field(default=UNSET, alias="inputQty")
    """Quantity of an item that is input by the seller"""

    avail_to_sell_qty: Optional[AvailToSellQty] = Field(default=UNSET, alias="availToSellQty")
    """Quantity of an item that is available to be allocated to orders."""

    reserved_qty: Optional[SupplyQuantity] = Field(default=UNSET, alias="reservedQty")
    """Quantity that has been ordered by the customers but not yet shipped."""


class GetAllInventoriesNodeDtoDict(TypedDict):
    ship_node: NotRequired[str]
    input_qty: NotRequired[InputQtyDict]
    avail_to_sell_qty: NotRequired[AvailToSellQtyDict]
    reserved_qty: NotRequired[SupplyQuantityDict]
