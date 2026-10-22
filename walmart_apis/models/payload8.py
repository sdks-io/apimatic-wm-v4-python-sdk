from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .inventory_wfs import InventoryWfs, InventoryWfsDict


class Payload8(SdkBaseModel):
    inventory: Optional[list[InventoryWfs]] = UNSET


class Payload8Dict(TypedDict):
    inventory: NotRequired[list[InventoryWfsDict]]
