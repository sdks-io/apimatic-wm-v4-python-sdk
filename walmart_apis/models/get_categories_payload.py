from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .product_type import ProductType, ProductTypeDict


class GetCategoriesPayload(SdkBaseModel):
    name: Optional[str] = UNSET
    count: Optional[int] = UNSET
    product_type: Optional[list[ProductType]] = Field(default=UNSET, alias="productType")
    """productType is only applicable for categories"""


class GetCategoriesPayloadDict(TypedDict):
    name: NotRequired[str]
    count: NotRequired[int]
    product_type: NotRequired[list[ProductTypeDict]]
