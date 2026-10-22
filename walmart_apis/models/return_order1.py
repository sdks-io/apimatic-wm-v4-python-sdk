from __future__ import annotations

from pydantic import EmailStr, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .customer_name1 import CustomerName1, CustomerName1Dict
from .return_order_line1 import ReturnOrderLine1, ReturnOrderLine1Dict
from .return_order_shipment1 import ReturnOrderShipment1, ReturnOrderShipment1Dict


class ReturnOrder1(SdkBaseModel):
    return_order_id: Optional[str] = Field(default=UNSET, alias="returnOrderId")
    """returnOrderId.<br><b style='color:green;'>Market availability: MX</b>"""

    customer_order_id: Optional[str] = Field(default=UNSET, alias="customerOrderId")
    """customerOrderId.<br><b style='color:green;'>Market availability: MX</b>"""

    customer_email: Optional[EmailStr] = Field(default=UNSET, alias="customerEmail")
    """customerEmail.<br><b style='color:green;'>Market availability: MX</b>"""

    return_order_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="returnOrderDate")
    """returnOrderDate.<br><b style='color:green;'>Market availability: MX | CA |CL</b>"""

    customer_name: Optional[CustomerName1] = Field(default=UNSET, alias="customerName")
    """customerName.<br><b style='color:green;'>Market availability: MX</b>"""

    return_order_lines: Optional[list[ReturnOrderLine1]] = Field(default=UNSET, alias="returnOrderLines")
    """returnOrderLines.<br><b style='color:green;'>Market availability: MX</b>"""

    return_order_shipments: Optional[list[ReturnOrderShipment1]] = Field(default=UNSET, alias="returnOrderShipments")
    """returnOrderShipments.<br><b style='color:green;'>Market availability: MX</b>"""


class ReturnOrder1Dict(TypedDict):
    return_order_id: NotRequired[str]
    customer_order_id: NotRequired[str]
    customer_email: NotRequired[EmailStr]
    return_order_date: NotRequired[RFC3339DateTime]
    customer_name: NotRequired[CustomerName1Dict]
    return_order_lines: NotRequired[list[ReturnOrderLine1Dict]]
    return_order_shipments: NotRequired[list[ReturnOrderShipment1Dict]]
