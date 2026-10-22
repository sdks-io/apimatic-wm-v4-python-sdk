from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .add_ons_response import AddOnsResponse, AddOnsResponseDict
from .box_item import BoxItem, BoxItemDict


class LabelGenerationResponse(SdkBaseModel):
    """Response payload containing the label tracking details for a single shipment."""

    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    """Purchase Order Id"""

    tracking_no: Optional[str] = Field(default=UNSET, alias="trackingNo")
    """Tracking Number"""

    box_items: Optional[list[BoxItem]] = Field(default=UNSET, alias="boxItems")
    """Box Items"""

    carrier_name: Optional[str] = Field(default=UNSET, alias="carrierName")
    """Carrier Short Name"""

    carrier_full_name: Optional[str] = Field(default=UNSET, alias="carrierFullName")
    """Carrier Full Name"""

    carrier_service_type: Optional[str] = Field(default=UNSET, alias="carrierServiceType")
    """Carrier Service Type"""

    tracking_url: Optional[str] = Field(default=UNSET, alias="trackingUrl")
    """Tracking URL"""

    add_ons: Optional[list[AddOnsResponse]] = Field(default=UNSET, alias="addOns")
    """Add Ons Response"""


class LabelGenerationResponseDict(TypedDict):
    purchase_order_id: NotRequired[str]
    tracking_no: NotRequired[str]
    box_items: NotRequired[list[BoxItemDict]]
    carrier_name: NotRequired[str]
    carrier_full_name: NotRequired[str]
    carrier_service_type: NotRequired[str]
    tracking_url: NotRequired[str]
    add_ons: NotRequired[list[AddOnsResponseDict]]
