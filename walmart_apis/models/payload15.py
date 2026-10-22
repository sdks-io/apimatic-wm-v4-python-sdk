from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .replenishment import Replenishment, ReplenishmentDict


class Payload15(SdkBaseModel):
    replenishments: Optional[list[Replenishment]] = UNSET


class Payload15Dict(TypedDict):
    replenishments: NotRequired[list[ReplenishmentDict]]
