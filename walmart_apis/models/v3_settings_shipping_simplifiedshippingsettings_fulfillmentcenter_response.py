from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .simplified_shipping_settings7 import SimplifiedShippingSettings7, SimplifiedShippingSettings7Dict


class V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterResponse(SdkBaseModel):
    simplified_shipping_settings: Optional[SimplifiedShippingSettings7] = Field(
        default=UNSET, alias="simplifiedShippingSettings"
    )
    """Simplified Shipping Settings. <br><b style='color:green;'>Market availability: US</span></b>"""


class V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterResponseDict(TypedDict):
    simplified_shipping_settings: NotRequired[SimplifiedShippingSettings7Dict]
