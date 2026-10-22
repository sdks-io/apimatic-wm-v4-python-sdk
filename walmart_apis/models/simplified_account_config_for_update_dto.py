from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .carrier_config_dto import CarrierConfigDto, CarrierConfigDtoDict


class SimplifiedAccountConfigForUpdateDto(SdkBaseModel):
    """Account configuration to be set for a seller, comprising of Carrier configurations and Region configurations."""

    migrate_eligible_offers: Optional[bool] = Field(default=UNSET, alias="migrateEligibleOffers")
    """Flag used to migrate/not migrate all the eligible offers for a seller."""

    carrier_configs: Optional[list[CarrierConfigDto]] = Field(default=UNSET, alias="carrierConfigs")
    """Defines the carrier configurations used for shipping, like carrier details and their corresponding region
    coverage.."""


class SimplifiedAccountConfigForUpdateDtoDict(TypedDict):
    migrate_eligible_offers: NotRequired[bool]
    carrier_configs: NotRequired[list[CarrierConfigDtoDict]]
