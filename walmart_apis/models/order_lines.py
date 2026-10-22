from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .order_line import OrderLine, OrderLineDict


class OrderLines(SdkBaseModel):
    """Array of Order lines.<br><b style='color:green;'>Market availability: MX</b>"""

    order_line: Optional[list[OrderLine]] = Field(default=UNSET, alias="orderLine")


class OrderLinesDict(TypedDict):
    order_line: NotRequired[list[OrderLineDict]]
