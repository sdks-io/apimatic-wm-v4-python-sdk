from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .customer_name import CustomerName, CustomerNameDict
from .return_channel import ReturnChannel, ReturnChannelDict
from .return_line_group import ReturnLineGroup, ReturnLineGroupDict
from .return_order_line import ReturnOrderLine, ReturnOrderLineDict
from .return_order_shipment import ReturnOrderShipment, ReturnOrderShipmentDict
from .total_refund_amount import TotalRefundAmount, TotalRefundAmountDict


class ReturnOrder(SdkBaseModel):
    """List of returns for the seller.<br><b style='color:green;'>Market availability: Global</b>"""

    return_order_id: Optional[str] = Field(default=UNSET, alias="returnOrderId")
    """Return order identifier of the return order.<br><b style='color:green;'>Market availability: Global</b>"""

    customer_email_id: Optional[str] = Field(default=UNSET, alias="customerEmailId")
    """Customer email address<br><b style='color:green;'>Market availability: Global</b>"""

    customer_name: Optional[CustomerName] = Field(default=UNSET, alias="customerName")
    """Customer information.<br><b style='color:green;'>Market availability: Global</b>"""

    customer_order_id: Optional[str] = Field(default=UNSET, alias="customerOrderId")
    """Customer sales order identifier. Use to filter results.<br><b style='color:green;'>Market availability:
    Global</b>"""

    return_order_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="returnOrderDate")
    """Date format for return order date.<br><b style='color:green;'>Market availability: Global</b>"""

    return_by_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="returnByDate")
    """Date format for return by order date.<br><b style='color:green;'>Market availability: US</b>"""

    refund_mode: Optional[str] = Field(default=UNSET, alias="refundMode")
    """Determines when the refund was/will be issued to the customer.<br><b style='color:green;'>Market availability:
    US</b>"""

    total_refund_amount: Optional[TotalRefundAmount] = Field(default=UNSET, alias="totalRefundAmount")
    """Price of One unit of item, in this order line.<br><b style='color:green;'>Market availability: US</b>"""

    return_line_groups: Optional[list[ReturnLineGroup]] = Field(default=UNSET, alias="returnLineGroups")
    """These groups are created per label or type of carrier service required. (e.g., If order has some lines that can
    be clubbed and mailed together as a smart post then they belong to one return group. If a line is bulky and needs a
    different type of carrier service, then that line will be part of different group. Customer gets multiple labels
    depending on how many groups are created for the entire order.)<br><b style='color:green;'>Market availability:
    US</b>"""

    return_order_lines: Optional[list[ReturnOrderLine]] = Field(default=UNSET, alias="returnOrderLines")
    """A list of order lines in the return order.<br><b style='color:green;'>Market availability: Global</b>"""

    return_order_shipments: Optional[list[ReturnOrderShipment]] = Field(default=UNSET, alias="returnOrderShipments")
    """The shipments for return orders.<br><b style='color:green;'>Market availability: MX</b>"""

    return_channel: Optional[ReturnChannel] = Field(default=UNSET, alias="returnChannel")
    """The channel via order return got initiated.<br><b style='color:green;'>Market availability: US</b>"""


class ReturnOrderDict(TypedDict):
    return_order_id: NotRequired[str]
    customer_email_id: NotRequired[str]
    customer_name: NotRequired[CustomerNameDict]
    customer_order_id: NotRequired[str]
    return_order_date: NotRequired[RFC3339DateTime]
    return_by_date: NotRequired[RFC3339DateTime]
    refund_mode: NotRequired[str]
    total_refund_amount: NotRequired[TotalRefundAmountDict]
    return_line_groups: NotRequired[list[ReturnLineGroupDict]]
    return_order_lines: NotRequired[list[ReturnOrderLineDict]]
    return_order_shipments: NotRequired[list[ReturnOrderShipmentDict]]
    return_channel: NotRequired[ReturnChannelDict]
