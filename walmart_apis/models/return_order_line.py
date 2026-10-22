from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .charge import Charge, ChargeDict
from .gmv import Gmv, GmvDict
from .item2 import Item2, Item2Dict


class ReturnOrderLine(SdkBaseModel):
    """A list of order lines in the return order.<br><b style='color:green;'>Market availability: Global</b>"""

    return_order_line_number: Optional[int] = Field(default=UNSET, alias="returnOrderLineNumber")
    """The returns order line number for that return.<br><b style='color:green;'>Market availability: Global</b>"""

    prime_line_number: Optional[str] = Field(default=UNSET, alias="primeLineNumber")
    """The purchase order line number for the return created.<br><b style='color:green;'>Market availability: MX | CA |
    CL</b>"""

    sales_order_line_number: Optional[int] = Field(default=UNSET, alias="salesOrderLineNumber")
    """The sales order line number for the return created.<br><b style='color:green;'>Market availability: US</b>"""

    return_reason: Optional[str] = Field(default=UNSET, alias="returnReason")
    """Gives the reason that was selected during the return creation.<br><b style='color:green;'>Market availability:
    Global</b>"""

    reason_code: Optional[str] = Field(default=UNSET, alias="reasonCode")
    """Gives the return reason code associated with returnReason.<br><b style='color:green;'>Market availability:
    MX</b>"""

    return_description: Optional[str] = Field(default=UNSET, alias="returnDescription")
    """Gives the returnDescription for the return created. It would be empty if returnDescription is 'Fraud'.<br><b
    style='color:green;'>Market availability: US</b>"""

    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    """The purchase order ID for the return created.<br><b style='color:green;'>Market availability: Global</b>"""

    purchase_order_line_number: Optional[int] = Field(default=UNSET, alias="purchaseOrderLineNumber")
    """The purchase order line number for the return created.<br><b style='color:green;'>Market
    availability:Global</b>"""

    is_return_for_exception: Optional[bool] = Field(default=UNSET, alias="isReturnForException")
    """<b style='color:green;'>Market availability: US</b>"""

    item: Optional[Item2] = UNSET
    """An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item.<br><b
    style='color:green;'>Market availability: Global</b>"""

    charges: Optional[list[Charge]] = UNSET
    """Information relating to the charge for the orderLine.<br><b style='color:green;'>Market availability: US |
    MX</b>"""

    status: Optional[str] = UNSET
    """Current status of return. (e.g., 'INITIATED') <br><b style='color:green;'>Market availability: MX | CA |CL</b>"""

    refund_amount: Optional[Gmv] = Field(default=UNSET, alias="refundAmount")
    """Refund amount details for the return order line.<br><b style='color:green;'>Market availability: MX | CA |
    CL</b>"""

    is_wfs_enabled: Optional[str] = Field(default=UNSET, alias="isWFSEnabled")
    """Determines Walmart Fulfilled vs Seller Fulfilled returns.<br><b style='color:green;'>Market availability: MX | CA
    | CL</b>"""


class ReturnOrderLineDict(TypedDict):
    return_order_line_number: NotRequired[int]
    prime_line_number: NotRequired[str]
    sales_order_line_number: NotRequired[int]
    return_reason: NotRequired[str]
    reason_code: NotRequired[str]
    return_description: NotRequired[str]
    purchase_order_id: NotRequired[str]
    purchase_order_line_number: NotRequired[int]
    is_return_for_exception: NotRequired[bool]
    item: NotRequired[Item2Dict]
    charges: NotRequired[list[ChargeDict]]
    status: NotRequired[str]
    refund_amount: NotRequired[GmvDict]
    is_wfs_enabled: NotRequired[str]
