from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .simplified_account_shipping_settings_for_update_dto import (
    SimplifiedAccountShippingSettingsForUpdateDto,
    SimplifiedAccountShippingSettingsForUpdateDtoDict,
)


class UpdateSimplifiedShippingSettingsRequest(SdkBaseModel):
    simplified_shipping_settings: Optional[SimplifiedAccountShippingSettingsForUpdateDto] = Field(
        default=UNSET, alias="simplifiedShippingSettings"
    )
    """Simplified Shipping Settings"""


class UpdateSimplifiedShippingSettingsRequestDict(TypedDict):
    simplified_shipping_settings: NotRequired[SimplifiedAccountShippingSettingsForUpdateDtoDict]
