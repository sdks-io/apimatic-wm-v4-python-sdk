from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .ship_nodes2 import ShipNodes2, ShipNodes2Dict


class Inventory3(SdkBaseModel):
    sku: Optional[str] = UNSET
    """An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item."""

    ship_nodes: Optional[list[ShipNodes2]] = Field(default=UNSET, alias="shipNodes")


class Inventory3Dict(TypedDict):
    sku: NotRequired[str]
    ship_nodes: NotRequired[list[ShipNodes2Dict]]
