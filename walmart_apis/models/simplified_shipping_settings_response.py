from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .simplified_shipping_settings_dto import SimplifiedShippingSettingsDto, SimplifiedShippingSettingsDtoDict


class SimplifiedShippingSettingsResponse(SdkBaseModel):
    simplified_shipping_settings: Optional[SimplifiedShippingSettingsDto] = Field(
        default=UNSET, alias="simplifiedShippingSettings"
    )
    """Simplified Shipping Settings"""


class SimplifiedShippingSettingsResponseDict(TypedDict):
    simplified_shipping_settings: NotRequired[SimplifiedShippingSettingsDtoDict]
