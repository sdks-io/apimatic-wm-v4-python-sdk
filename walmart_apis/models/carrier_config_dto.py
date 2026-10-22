from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .automated_shipping_settings_configuration_dto import (
    AutomatedShippingSettingsConfigurationDto,
    AutomatedShippingSettingsConfigurationDtoDict,
)
from .carrier_dto import CarrierDto, CarrierDtoDict


class CarrierConfigDto(SdkBaseModel):
    """List of Fulfillment Center Ids which are used as shipping nodes."""

    is_default: Optional[bool] = Field(default=UNSET, alias="isDefault")
    configurations: Optional[list[AutomatedShippingSettingsConfigurationDto]] = UNSET
    """Defines the carrier configurations used for shipping, like carrier details and their corresponding region
    coverage.."""

    carriers: Optional[list[CarrierDto]] = UNSET
    """Defines the carrier configurations used for shipping, like carrier name and carrier service."""


class CarrierConfigDtoDict(TypedDict):
    is_default: NotRequired[bool]
    configurations: NotRequired[list[AutomatedShippingSettingsConfigurationDtoDict]]
    carriers: NotRequired[list[CarrierDtoDict]]
