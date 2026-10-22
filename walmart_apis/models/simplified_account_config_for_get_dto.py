from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .carrier_config_for_get_dto import CarrierConfigForGetDto, CarrierConfigForGetDtoDict
from .enums.shipping_priority import ShippingPriorityOrStr


class SimplifiedAccountConfigForGetDto(SdkBaseModel):
    """Account configuration to be set for a seller, comprising of Carrier configurations and Region configurations."""

    shipping_priority: Optional[ShippingPriorityOrStr] = Field(default=UNSET, alias="shippingPriority")
    """Shipping priority will help system decide the carrier service for fulfillment in case there are multiple shipping
    options available for customers with different carrier services in terms of shipping cost and speed."""

    migrate_eligible_offers: Optional[bool] = Field(default=UNSET, alias="migrateEligibleOffers")
    """Flag used to migrate/not migrate all the eligible offers for a seller."""

    carrier_configs: Optional[list[CarrierConfigForGetDto]] = Field(default=UNSET, alias="carrierConfigs")
    """Defines the carrier configurations used for shipping, like carrier details and their corresponding region
    coverage.."""


class SimplifiedAccountConfigForGetDtoDict(TypedDict):
    shipping_priority: NotRequired[ShippingPriorityOrStr]
    migrate_eligible_offers: NotRequired[bool]
    carrier_configs: NotRequired[list[CarrierConfigForGetDtoDict]]
