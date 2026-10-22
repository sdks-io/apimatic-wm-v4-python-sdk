from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .simplified_account_shipping_settings_dto import (
    SimplifiedAccountShippingSettingsDto,
    SimplifiedAccountShippingSettingsDtoDict,
)


class CreateSimplifiedShippingSettingsRequest(SdkBaseModel):
    simplified_shipping_settings: Optional[SimplifiedAccountShippingSettingsDto] = Field(
        default=UNSET, alias="simplifiedShippingSettings"
    )
    """Simplified Shipping Settings"""


class CreateSimplifiedShippingSettingsRequestDict(TypedDict):
    simplified_shipping_settings: NotRequired[SimplifiedAccountShippingSettingsDtoDict]
