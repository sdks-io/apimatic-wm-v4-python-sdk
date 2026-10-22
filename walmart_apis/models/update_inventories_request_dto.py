from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .update_inventories_request_node_dto import UpdateInventoriesRequestNodeDto, UpdateInventoriesRequestNodeDtoDict


class UpdateInventoriesRequestDto(SdkBaseModel):
    nodes: list[UpdateInventoriesRequestNodeDto]


class UpdateInventoriesRequestDtoDict(TypedDict):
    nodes: list[UpdateInventoriesRequestNodeDtoDict]
