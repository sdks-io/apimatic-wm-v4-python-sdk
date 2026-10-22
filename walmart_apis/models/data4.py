from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .add_on8 import AddOn8, AddOn8Dict
from .box_item7 import BoxItem7, BoxItem7Dict


class Data4(SdkBaseModel):
    """Response payload containing the generated label tracking details and, when requested, the label file."""

    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    """The purchase order ID.

    <b style="color: green;">Market availability: Global</b>"""

    tracking_no: Optional[str] = Field(default=UNSET, alias="trackingNo")
    """Tracking Number

    <b style="color: green;">Market availability: Global</b>"""

    box_items: Optional[list[BoxItem7]] = Field(default=UNSET, alias="boxItems")
    """Box Items

    <b style="color: green;">Market availability: Global</b>"""

    carrier_name: Optional[str] = Field(default=UNSET, alias="carrierName")
    """Carrier short name.

    <b style="color: green;">Market availability: Global</b>"""

    carrier_full_name: Optional[str] = Field(default=UNSET, alias="carrierFullName")
    """Carrier full name.

    <b style="color: green;">Market availability: Global </b>"""

    carrier_service_type: Optional[str] = Field(default=UNSET, alias="carrierServiceType")
    """Carrier service type.

    <b style="color: green;">Market availability: Global</b>"""

    tracking_url: Optional[str] = Field(default=UNSET, alias="trackingUrl")
    """Tracking URL.

    <b style="color: green;">Market availability: Global</b>"""

    add_ons: Optional[list[AddOn8]] = Field(default=UNSET, alias="addOns")
    """Add-on response items.

    <b style="color: green;">Market availability: US only</b>"""


class Data4Dict(TypedDict):
    purchase_order_id: NotRequired[str]
    tracking_no: NotRequired[str]
    box_items: NotRequired[list[BoxItem7Dict]]
    carrier_name: NotRequired[str]
    carrier_full_name: NotRequired[str]
    carrier_service_type: NotRequired[str]
    tracking_url: NotRequired[str]
    add_ons: NotRequired[list[AddOn8Dict]]
