from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .quantity5 import Quantity5, Quantity5Dict


class V3InventoryRequest(SdkBaseModel):
    sku: str
    """A seller-provided Product ID. Response will have decoded value.

    <strong style="color: green;">Market availability: Global</strong>"""

    quantity: Quantity5
    """Quantity that has been ordered by the customers but not yet shipped.

    <strong style="color: green;">Market availability: Global</strong>"""

    inventory_available_date: Optional[str] = Field(default=UNSET, alias="inventoryAvailableDate")
    """Information about when the inventory is expected at the given ship node. Format:YYYY-MM-DD

    <strong style="color: green;">Market availability: US only</strong>"""


class V3InventoryRequestDict(TypedDict):
    sku: str
    quantity: Quantity5Dict
    inventory_available_date: NotRequired[str]
