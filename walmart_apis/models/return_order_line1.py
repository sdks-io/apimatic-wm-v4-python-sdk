from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .charge1 import Charge1, Charge1Dict
from .gmv import Gmv, GmvDict
from .item12 import Item12, Item12Dict
from .quantity1 import Quantity1, Quantity1Dict


class ReturnOrderLine1(SdkBaseModel):
    return_order_line_number: Optional[str] = Field(default=UNSET, alias="returnOrderLineNumber")
    """returnOrderLineNumber.<br><b style='color:green;'>Market availability: MX</b>"""

    prime_line_number: Optional[str] = Field(default=UNSET, alias="primeLineNumber")
    """primeLineNumber.<br><b style='color:green;'>Market availability: MX</b>"""

    return_reason: Optional[str] = Field(default=UNSET, alias="returnReason")
    """returnReason.<br><b style='color:green;'>Market availability: MX</b>"""

    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    """purchaseOrderId.<br><b style='color:green;'>Market availability: MX</b>"""

    purchase_order_line_number: Optional[str] = Field(default=UNSET, alias="purchaseOrderLineNumber")
    """purchaseOrderLineNumber.<br><b style='color:green;'>Market availability: MX</b>"""

    item: Optional[Item12] = UNSET
    """item.<br><b style='color:green;'>Market availability: MX</b>"""

    charges: Optional[list[Charge1]] = UNSET
    """charges.<br><b style='color:green;'>Market availability: MX</b>"""

    unit_price: Optional[Gmv] = Field(default=UNSET, alias="unitPrice")
    """unitPrice.<br><b style='color:green;'>Market availability: MX</b>"""

    quantity: Optional[Quantity1] = UNSET
    """quantity.<br><b style='color:green;'>Market availability: MX</b>"""

    status: Optional[str] = UNSET
    """Current status of return. (e.g., 'INITIATED') <br><b style='color:green;'>Market availability: MX</b>"""

    status_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="statusTime")
    """statusTime.<br><b style='color:green;'>Market availability: MX</b>"""

    refund_amount: Optional[Gmv] = Field(default=UNSET, alias="refundAmount")
    """refundAmount.<br><b style='color:green;'>Market availability: MX</b>"""

    is_wfs_enabled: Optional[str] = Field(default=UNSET, alias="isWFSEnabled")
    """isWFSEnabled.<br><b style='color:green;'>Market availability: MX</b>"""


class ReturnOrderLine1Dict(TypedDict):
    return_order_line_number: NotRequired[str]
    prime_line_number: NotRequired[str]
    return_reason: NotRequired[str]
    purchase_order_id: NotRequired[str]
    purchase_order_line_number: NotRequired[str]
    item: NotRequired[Item12Dict]
    charges: NotRequired[list[Charge1Dict]]
    unit_price: NotRequired[GmvDict]
    quantity: NotRequired[Quantity1Dict]
    status: NotRequired[str]
    status_time: NotRequired[RFC3339DateTime]
    refund_amount: NotRequired[GmvDict]
    is_wfs_enabled: NotRequired[str]
