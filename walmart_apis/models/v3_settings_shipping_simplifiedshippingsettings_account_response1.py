from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .simplified_shipping_settings11 import SimplifiedShippingSettings11, SimplifiedShippingSettings11Dict


class V3SettingsShippingSimplifiedshippingsettingsAccountResponse1(SdkBaseModel):
    simplified_shipping_settings: Optional[SimplifiedShippingSettings11] = Field(
        default=UNSET, alias="simplifiedShippingSettings"
    )
    """Simplified Shipping Settings. <br><b style='color:green;'>Market availability: US</span></b>"""


class V3SettingsShippingSimplifiedshippingsettingsAccountResponse1Dict(TypedDict):
    simplified_shipping_settings: NotRequired[SimplifiedShippingSettings11Dict]
