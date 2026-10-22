from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .simplified_shipping_settings10 import SimplifiedShippingSettings10, SimplifiedShippingSettings10Dict


class V3SettingsShippingSimplifiedshippingsettingsAccountRequest1(SdkBaseModel):
    simplified_shipping_settings: Optional[SimplifiedShippingSettings10] = Field(
        default=UNSET, alias="simplifiedShippingSettings"
    )
    """Simplified Shipping Settings. <br><b style='color:green;'>Market availability: US</span></b>"""


class V3SettingsShippingSimplifiedshippingsettingsAccountRequest1Dict(TypedDict):
    simplified_shipping_settings: NotRequired[SimplifiedShippingSettings10Dict]
