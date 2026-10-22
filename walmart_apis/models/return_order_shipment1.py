from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReturnOrderShipment1(SdkBaseModel):
    shipment_no: Optional[str] = Field(default=UNSET, alias="shipmentNo")
    """shipmentNo.<br><b style='color:green;'>Market availability: MX</b>"""

    tracking_number: Optional[str] = Field(default=UNSET, alias="trackingNumber")
    """trackingNumber.<br><b style='color:green;'>Market availability: MX</b>"""


class ReturnOrderShipment1Dict(TypedDict):
    shipment_no: NotRequired[str]
    tracking_number: NotRequired[str]
