from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .node_dto import NodeDto, NodeDtoDict


class V3Inventories400Error(SdkBaseModel):
    sku: Optional[str] = UNSET
    """An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item."""

    nodes: Optional[list[NodeDto]] = UNSET


class V3Inventories400ErrorDict(TypedDict):
    sku: NotRequired[str]
    nodes: NotRequired[list[NodeDtoDict]]
