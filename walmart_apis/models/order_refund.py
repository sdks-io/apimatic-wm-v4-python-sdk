from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .order_lines import OrderLines, OrderLinesDict


class OrderRefund(SdkBaseModel):
    """Array orderRefund.<br><b style='color:green;'>Market availability: MX</b>"""

    order_lines: Optional[OrderLines] = Field(default=UNSET, alias="orderLines")
    """Array of Order lines.<br><b style='color:green;'>Market availability: MX</b>"""


class OrderRefundDict(TypedDict):
    order_lines: NotRequired[OrderLinesDict]
