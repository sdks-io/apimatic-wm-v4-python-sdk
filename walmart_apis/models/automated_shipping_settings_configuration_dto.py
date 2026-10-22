from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.address_type import AddressTypeOrStr
from .region_dto import RegionDto, RegionDtoDict


class AutomatedShippingSettingsConfigurationDto(SdkBaseModel):
    """Defines the carrier configurations used for shipping, like carrier details and their corresponding region
    coverage.."""

    regions: Optional[list[RegionDto]] = UNSET
    """Region configurations to which shipping has to be covered with added carriers."""

    address_types: Optional[list[AddressTypeOrStr]] = Field(default=UNSET, alias="addressTypes")
    """Type of address to which shipping has to be covered as part of mentioned region, sub region and states."""


class AutomatedShippingSettingsConfigurationDtoDict(TypedDict):
    regions: NotRequired[list[RegionDtoDict]]
    address_types: NotRequired[list[AddressTypeOrStr]]
