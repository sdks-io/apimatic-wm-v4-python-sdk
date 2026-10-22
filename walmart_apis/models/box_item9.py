from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BoxItem9(SdkBaseModel):
    """Box Items"""

    sku: str
    """sku of an item"""

    quantity: int
    """Quantity of Item"""

    line_number: str = Field(alias="lineNumber")
    """primeLineNo from CA order's response"""


class BoxItem9Dict(TypedDict):
    sku: str
    quantity: int
    line_number: str
