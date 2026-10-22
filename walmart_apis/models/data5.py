from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .box_item9 import BoxItem9, BoxItem9Dict
from .other_label import OtherLabel, OtherLabelDict
from .shipping_documents import ShippingDocuments, ShippingDocumentsDict


class Data5(SdkBaseModel):
    """data"""

    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    """Purchase Order Id"""

    id: Optional[str] = UNSET
    """shipmentId"""

    tracking_no: Optional[str] = Field(default=UNSET, alias="trackingNo")
    """Tracking Number"""

    box_items: Optional[list[BoxItem9]] = Field(default=UNSET, alias="boxItems")
    """Box Items"""

    carrier_name: Optional[str] = Field(default=UNSET, alias="carrierName")
    """Carrier Short Name"""

    carrier_full_name: Optional[str] = Field(default=UNSET, alias="carrierFullName")
    """Carrier Full Name"""

    carrier_service_type: Optional[str] = Field(default=UNSET, alias="carrierServiceType")
    """Carrier Service Type. It wont be present for Purolator."""

    tracking_url: Optional[str] = Field(default=UNSET, alias="trackingUrl")
    """Tracking URL"""

    shipping_documents: Optional[ShippingDocuments] = Field(default=UNSET, alias="shippingDocuments")
    """Shipping Documents"""

    other_labels: Optional[list[OtherLabel]] = Field(default=UNSET, alias="otherLabels")
    """Child labels for multi package label"""


class Data5Dict(TypedDict):
    purchase_order_id: NotRequired[str]
    id: NotRequired[str]
    tracking_no: NotRequired[str]
    box_items: NotRequired[list[BoxItem9Dict]]
    carrier_name: NotRequired[str]
    carrier_full_name: NotRequired[str]
    carrier_service_type: NotRequired[str]
    tracking_url: NotRequired[str]
    shipping_documents: NotRequired[ShippingDocumentsDict]
    other_labels: NotRequired[list[OtherLabelDict]]
