from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ShipNodes(SdkBaseModel):
    modified_date: Optional[str] = Field(default=UNSET, alias="modifiedDate")
    """Last changes date for the item."""

    avail_to_sell_qty: Optional[int] = Field(default=UNSET, alias="availToSellQty")
    """The available quantity is the Quantity of an item that is available to be allocated to orders."""

    on_hand_qty: Optional[int] = Field(default=UNSET, alias="onHandQty")
    """The on-hand balance is the quantity of active inventory stored at the warehouse.Active inventory is defined as
    the usable amount of an item that is in the warehouse.Inventory is active if it is not damaged, expired or being
    inspected."""

    ship_node_type: Optional[str] = Field(default=UNSET, alias="shipNodeType")
    """Identifies fulfillment aspect of invetory. Walmart, seller or 3PL fulfilled. Possible value is 'WFSFulfilled'. In
    later phase we will also add seller fulfilled inventory."""


class ShipNodesDict(TypedDict):
    modified_date: NotRequired[str]
    avail_to_sell_qty: NotRequired[int]
    on_hand_qty: NotRequired[int]
    ship_node_type: NotRequired[str]
