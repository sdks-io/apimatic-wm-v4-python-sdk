from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .quantity import Quantity, QuantityDict


class RefundLine(SdkBaseModel):
    """A line number associated with each individual line in the return order. If return order has only one return order
    line and it is not provided in the request, the only available return order line is auto-selected. If return order
    has multiple return order lines, the required return order line must be provided in the request. If not provided in
    the request, it will result in data-error..<br><b style='color:green;'>Market availability: US</b>"""

    return_order_line_number: int = Field(alias="returnOrderLineNumber")
    quantity: Quantity
    """Total quantity returned in this return line.>"""


class RefundLineDict(TypedDict):
    return_order_line_number: int
    quantity: QuantityDict
