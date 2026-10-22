from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SupplierItemOrderable(SdkBaseModel):
    product_id: str = Field(alias="productId")
    """Product GTIN (Global Trade Item Number) — the unique product identifier."""


class SupplierItemOrderableDict(TypedDict):
    product_id: str
