from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.field6 import Field6OrStr


class SearchRequest(SdkBaseModel):
    """Search request."""

    field: Optional[Field6OrStr] = UNSET
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ITEM_NAME | Product name | string |
    | SKU | Specifies the item identified. This value is defined by the seller. | string |"""

    value: Optional[str] = UNSET


class SearchRequestDict(TypedDict):
    field: NotRequired[Field6OrStr]
    value: NotRequired[str]
