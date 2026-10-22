from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.item_status5 import ItemStatus5OrStr


class GetCategoriesRequest(SdkBaseModel):
    item_status: Optional[ItemStatus5OrStr] = Field(default=UNSET, alias="itemStatus")
    """IRP status of the items."""


class GetCategoriesRequestDict(TypedDict):
    item_status: NotRequired[ItemStatus5OrStr]
