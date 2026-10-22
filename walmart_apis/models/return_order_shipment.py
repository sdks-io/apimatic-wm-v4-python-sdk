from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReturnOrderShipment(SdkBaseModel):
    shipment_no: Optional[str] = Field(default=UNSET, alias="shipmentNo")
    """The unique number for the shipment line in a given shipment.<br><b style='color:green;'>Market availability:
    MX</b>"""

    tracking_number: Optional[str] = Field(default=UNSET, alias="trackingNumber")
    """The unique number for tracking.<br><b style='color:green;'>Market availability: MX</b>"""


class ReturnOrderShipmentDict(TypedDict):
    shipment_no: NotRequired[str]
    tracking_number: NotRequired[str]
