from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .simplified_fcshipping_settings_dto import SimplifiedFcshippingSettingsDto, SimplifiedFcshippingSettingsDtoDict


class UpdateFclevelSimplifiedShippingSettingsRequest(SdkBaseModel):
    simplified_shipping_settings: Optional[SimplifiedFcshippingSettingsDto] = Field(
        default=UNSET, alias="simplifiedShippingSettings"
    )
    """Simplified Shipping Settings"""


class UpdateFclevelSimplifiedShippingSettingsRequestDict(TypedDict):
    simplified_shipping_settings: NotRequired[SimplifiedFcshippingSettingsDtoDict]
