from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EstimatesBoxItem(SdkBaseModel):
    """Box items. This is a mandatory field for India(IN) to United States(US) shipping"""

    sku: str
    """sku of an item"""

    quantity: int
    """Quantity of Item"""

    line_number: str = Field(alias="lineNumber")
    """PO Line Number"""


class EstimatesBoxItemDict(TypedDict):
    sku: str
    quantity: int
    line_number: str
