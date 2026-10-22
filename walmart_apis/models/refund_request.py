from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .order_refund import OrderRefund, OrderRefundDict
from .refund_line import RefundLine, RefundLineDict


class RefundRequest(SdkBaseModel):
    customer_order_id: str = Field(alias="customerOrderId")
    """A unique ID associated with the sales order for specified customer.<br><b style='color:green;'>Market
    availability: US | MX</b>"""

    refund_lines: list[RefundLine] = Field(alias="refundLines")
    """Array of refund lines.<br><b style='color:green;'>Market availability: US</b>"""

    order_refund: OrderRefund = Field(alias="orderRefund")
    """Array orderRefund.<br><b style='color:green;'>Market availability: MX</b>"""


class RefundRequestDict(TypedDict):
    customer_order_id: str
    refund_lines: list[RefundLineDict]
    order_refund: OrderRefundDict
