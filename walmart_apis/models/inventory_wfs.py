from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .ship_nodes import ShipNodes, ShipNodesDict


class InventoryWfs(SdkBaseModel):
    sku: Optional[str] = UNSET
    """An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item."""

    ship_nodes: Optional[list[ShipNodes]] = Field(default=UNSET, alias="shipNodes")


class InventoryWfsDict(TypedDict):
    sku: NotRequired[str]
    ship_nodes: NotRequired[list[ShipNodesDict]]
