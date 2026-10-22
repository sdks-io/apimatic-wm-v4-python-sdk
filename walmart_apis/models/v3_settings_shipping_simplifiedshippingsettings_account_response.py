from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .simplified_shipping_settings9 import SimplifiedShippingSettings9, SimplifiedShippingSettings9Dict


class V3SettingsShippingSimplifiedshippingsettingsAccountResponse(SdkBaseModel):
    simplified_shipping_settings: Optional[SimplifiedShippingSettings9] = Field(
        default=UNSET, alias="simplifiedShippingSettings"
    )
    """Simplified Shipping Settings. <br><b style='color:green;'>Market availability: US</span></b>"""


class V3SettingsShippingSimplifiedshippingsettingsAccountResponseDict(TypedDict):
    simplified_shipping_settings: NotRequired[SimplifiedShippingSettings9Dict]
