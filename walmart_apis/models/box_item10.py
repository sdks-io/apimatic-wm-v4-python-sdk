from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BoxItem10(SdkBaseModel):
    """boxItems - A list of items that the seller will be shipping in this package. Each item must correspond to a line
    item in the specified purchaseOrder. The lineId and SKU fields are used to uniquely identify the specific item being
    shipped."""

    sku: str
    """sku of an item"""

    quantity: int
    """Quantity of Item"""

    line_number: str = Field(alias="lineNumber")
    """PO Line Number"""


class BoxItem10Dict(TypedDict):
    sku: str
    quantity: int
    line_number: str
