from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .inventory3 import Inventory3, Inventory3Dict


class Payload21(SdkBaseModel):
    inventory: Optional[list[Inventory3]] = UNSET


class Payload21Dict(TypedDict):
    inventory: NotRequired[list[Inventory3Dict]]
