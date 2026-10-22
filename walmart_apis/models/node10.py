from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .input_qty13 import InputQty13, InputQty13Dict


class Node10(SdkBaseModel):
    ship_node: str = Field(alias="shipNode")
    """Specifies the unique identifier of the ship node for which the inventory is requested.

    <strong style="color: green;">Market availability: Global</strong>"""

    input_qty: InputQty13 = Field(alias="inputQty")
    """Indicates the quantity that has been ordered by the customers but not yet shipped.

    <strong style="color: green;">Market availability: Global</strong>"""

    inventory_available_date: Optional[str] = Field(default=UNSET, alias="inventoryAvailableDate")
    """Specifies the date when the inventory will be available at a ship node. The date format is YYYY-MM-DD.

    <strong style="color: green;">Market availability: US only</strong>"""


class Node10Dict(TypedDict):
    ship_node: str
    input_qty: InputQty13Dict
    inventory_available_date: NotRequired[str]
