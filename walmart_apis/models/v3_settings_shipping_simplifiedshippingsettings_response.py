from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .simplified_shipping_settings12 import SimplifiedShippingSettings12, SimplifiedShippingSettings12Dict


class V3SettingsShippingSimplifiedshippingsettingsResponse(SdkBaseModel):
    simplified_shipping_settings: Optional[SimplifiedShippingSettings12] = Field(
        default=UNSET, alias="simplifiedShippingSettings"
    )
    """Simplified Shipping Settings. <br><b style='color:green;'>Market availability: US</span></b>"""


class V3SettingsShippingSimplifiedshippingsettingsResponseDict(TypedDict):
    simplified_shipping_settings: NotRequired[SimplifiedShippingSettings12Dict]
