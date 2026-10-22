from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .simplified_shipping_settings8 import SimplifiedShippingSettings8, SimplifiedShippingSettings8Dict


class V3SettingsShippingSimplifiedshippingsettingsAccountRequest(SdkBaseModel):
    simplified_shipping_settings: Optional[SimplifiedShippingSettings8] = Field(
        default=UNSET, alias="simplifiedShippingSettings"
    )
    """Simplified Shipping Settings. <br><b style='color:green;'>Market availability: US</span></b>"""


class V3SettingsShippingSimplifiedshippingsettingsAccountRequestDict(TypedDict):
    simplified_shipping_settings: NotRequired[SimplifiedShippingSettings8Dict]
