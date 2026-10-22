from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .update_inventories_response_node_dto import UpdateInventoriesResponseNodeDto, UpdateInventoriesResponseNodeDtoDict


class V3Inventories400Error2(SdkBaseModel):
    sku: Optional[str] = UNSET
    """An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item."""

    nodes: Optional[list[UpdateInventoriesResponseNodeDto]] = UNSET


class V3Inventories400Error2Dict(TypedDict):
    sku: NotRequired[str]
    nodes: NotRequired[list[UpdateInventoriesResponseNodeDtoDict]]
