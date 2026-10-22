from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_all_inventories_node_dto import GetAllInventoriesNodeDto, GetAllInventoriesNodeDtoDict


class GetAllInventoriesDto(SdkBaseModel):
    sku: Optional[str] = UNSET
    """An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item."""

    nodes: Optional[list[GetAllInventoriesNodeDto]] = UNSET


class GetAllInventoriesDtoDict(TypedDict):
    sku: NotRequired[str]
    nodes: NotRequired[list[GetAllInventoriesNodeDtoDict]]
