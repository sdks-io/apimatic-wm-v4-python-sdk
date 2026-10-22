from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.field12 import Field12OrStr
from .enums.order import OrderOrStr


class SortRequest(SdkBaseModel):
    """Sort request."""

    field: Optional[Field12OrStr] = UNSET
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ITEM_PRIORITY | Recommended priority of the item by Walmart. | integer |
    | PRICE | Item price | integer |"""

    order: Optional[OrderOrStr] = UNSET
    priority: Optional[int] = UNSET
    """Sort priority of the specified field."""


class SortRequestDict(TypedDict):
    field: NotRequired[Field12OrStr]
    order: NotRequired[OrderOrStr]
    priority: NotRequired[int]
