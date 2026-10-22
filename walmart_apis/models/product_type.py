from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ProductType(SdkBaseModel):
    """productType is only applicable for categories"""

    name: Optional[str] = UNSET
    count: Optional[int] = UNSET


class ProductTypeDict(TypedDict):
    name: NotRequired[str]
    count: NotRequired[int]
