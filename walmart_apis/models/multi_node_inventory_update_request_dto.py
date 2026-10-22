from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .update_inventories_request_dto import UpdateInventoriesRequestDto, UpdateInventoriesRequestDtoDict


class MultiNodeInventoryUpdateRequestDto(SdkBaseModel):
    inventories: UpdateInventoriesRequestDto


class MultiNodeInventoryUpdateRequestDtoDict(TypedDict):
    inventories: UpdateInventoriesRequestDtoDict
