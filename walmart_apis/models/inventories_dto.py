from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .node_dto import NodeDto, NodeDtoDict


class InventoriesDto(SdkBaseModel):
    sku: Optional[str] = UNSET
    """An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item."""

    nodes: Optional[list[NodeDto]] = UNSET


class InventoriesDtoDict(TypedDict):
    sku: NotRequired[str]
    nodes: NotRequired[list[NodeDtoDict]]
