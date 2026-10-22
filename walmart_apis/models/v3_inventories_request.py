from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .inventories3 import Inventories3, Inventories3Dict


class V3InventoriesRequest(SdkBaseModel):
    inventories: Inventories3
    """<strong style="color: green;">Market availability: Global</strong>"""


class V3InventoriesRequestDict(TypedDict):
    inventories: Inventories3Dict
