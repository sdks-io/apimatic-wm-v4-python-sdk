from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .add_ons_response import AddOnsResponse, AddOnsResponseDict
from .box_item11 import BoxItem11, BoxItem11Dict


class Data7(SdkBaseModel):
    """Label and tracking details for shipment in the purchase order."""

    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    """Purchase Order Id

    <b style="color: green;">Market availability: Global</b>"""

    tracking_no: Optional[str] = Field(default=UNSET, alias="trackingNo")
    """Tracking Number

    <b style="color: green;">Market availability: Global</b>"""

    box_items: Optional[list[BoxItem11]] = Field(default=UNSET, alias="boxItems")
    """Box Items

    <b style="color: green;">Market availability: Global</b>"""

    carrier_name: Optional[str] = Field(default=UNSET, alias="carrierName")
    """Carrier Short Name

    <b style="color: green;">Market availability: Global</b>"""

    carrier_full_name: Optional[str] = Field(default=UNSET, alias="carrierFullName")
    """Carrier Full Name

    <b style="color: green;">Market availability: Global</b>"""

    carrier_service_type: Optional[str] = Field(default=UNSET, alias="carrierServiceType")
    """Carrier Service Type

    <b style="color: green;">Market availability: Global</b>"""

    tracking_url: Optional[str] = Field(default=UNSET, alias="trackingUrl")
    """Tracking URL

    <b style="color: green;">Market availability: Global</b>"""

    add_ons: Optional[list[AddOnsResponse]] = Field(default=UNSET, alias="addOns")
    """Add Ons Response

    <b style="color: green;">Market availability: US only</b>"""


class Data7Dict(TypedDict):
    purchase_order_id: NotRequired[str]
    tracking_no: NotRequired[str]
    box_items: NotRequired[list[BoxItem11Dict]]
    carrier_name: NotRequired[str]
    carrier_full_name: NotRequired[str]
    carrier_service_type: NotRequired[str]
    tracking_url: NotRequired[str]
    add_ons: NotRequired[list[AddOnsResponseDict]]
