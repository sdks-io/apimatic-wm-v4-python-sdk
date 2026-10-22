from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .shipping_documents import ShippingDocuments, ShippingDocumentsDict


class OtherLabel(SdkBaseModel):
    """Child labels for multi package label"""

    tracking_no: Optional[str] = Field(default=UNSET, alias="trackingNo")
    """Tracking Number"""

    tracking_url: Optional[str] = Field(default=UNSET, alias="trackingUrl")
    """Tracking URL"""

    shipping_documents: Optional[list[ShippingDocuments]] = Field(default=UNSET, alias="shippingDocuments")
    """Shipping Documents"""


class OtherLabelDict(TypedDict):
    tracking_no: NotRequired[str]
    tracking_url: NotRequired[str]
    shipping_documents: NotRequired[list[ShippingDocumentsDict]]
