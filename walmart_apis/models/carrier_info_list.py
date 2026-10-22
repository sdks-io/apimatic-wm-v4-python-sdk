from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CarrierInfoList(SdkBaseModel):
    carrier_id: Optional[str] = Field(default=UNSET, alias="carrierId")
    """ID of the carrier used for the return.<br><b style='color:green;'>Market availability: US</b>"""

    carrier_name: Optional[str] = Field(default=UNSET, alias="carrierName")
    """Name of the carrier used.<br><b style='color:green;'>Market availability: US</b>"""

    service_type: Optional[str] = Field(default=UNSET, alias="serviceType")
    """The type of service used.<br><b style='color:green;'>Market availability: US</b>"""

    tracking_no: Optional[str] = Field(default=UNSET, alias="trackingNo")
    """Tracking number of the order.<br><b style='color:green;'>Market availability: US</b>"""


class CarrierInfoListDict(TypedDict):
    carrier_id: NotRequired[str]
    carrier_name: NotRequired[str]
    service_type: NotRequired[str]
    tracking_no: NotRequired[str]
