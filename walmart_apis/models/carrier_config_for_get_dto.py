from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .automated_shipping_settings_configuration_dto import (
    AutomatedShippingSettingsConfigurationDto,
    AutomatedShippingSettingsConfigurationDtoDict,
)
from .carrier_dto import CarrierDto, CarrierDtoDict


class CarrierConfigForGetDto(SdkBaseModel):
    """Defines the carrier configurations used for shipping, like carrier details and their corresponding region
    coverage.."""

    configurations: Optional[list[AutomatedShippingSettingsConfigurationDto]] = UNSET
    """Defines the carrier configurations used for shipping, like carrier details and their corresponding region
    coverage.."""

    carriers: Optional[list[CarrierDto]] = UNSET
    """Defines the carrier configurations used for shipping, like carrier name and carrier service."""


class CarrierConfigForGetDtoDict(TypedDict):
    configurations: NotRequired[list[AutomatedShippingSettingsConfigurationDtoDict]]
    carriers: NotRequired[list[CarrierDtoDict]]
