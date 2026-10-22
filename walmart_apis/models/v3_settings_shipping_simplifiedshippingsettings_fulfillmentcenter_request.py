from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .simplified_shipping_settings6 import SimplifiedShippingSettings6, SimplifiedShippingSettings6Dict


class V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequest(SdkBaseModel):
    simplified_shipping_settings: Optional[SimplifiedShippingSettings6] = Field(
        default=UNSET, alias="simplifiedShippingSettings"
    )
    """Simplified Shipping Settings. <br><b style='color:green;'>Market availability: US</span></b>"""


class V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequestDict(TypedDict):
    simplified_shipping_settings: NotRequired[SimplifiedShippingSettings6Dict]
