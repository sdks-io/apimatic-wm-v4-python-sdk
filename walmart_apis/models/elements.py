from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_all_inventories_dto import GetAllInventoriesDto, GetAllInventoriesDtoDict


class Elements(SdkBaseModel):
    inventories: Optional[list[GetAllInventoriesDto]] = UNSET


class ElementsDict(TypedDict):
    inventories: NotRequired[list[GetAllInventoriesDtoDict]]
