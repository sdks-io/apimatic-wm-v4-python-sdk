from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .carrier_config22 import CarrierConfig22, CarrierConfig22Dict
from .enums.shipping_priority7 import ShippingPriority7OrStr


class AccountConfigs11(SdkBaseModel):
    """Account configuration to be set for a seller, comprising of Carrier configurations and Region configurations.
    <br><b style='color:green;'>Market availability: US</span></b>"""

    shipping_priority: Optional[ShippingPriority7OrStr] = Field(default=UNSET, alias="shippingPriority")
    """Shipping priority will help system decide the carrier service for fulfillment in case there are multiple shipping
    options available for customers with different carrier services in terms of shipping cost and speed. <br><b
    style='color:green;'>Market availability: US</span></b>"""

    migrate_eligible_offers: Optional[bool] = Field(default=UNSET, alias="migrateEligibleOffers")
    """Flag used to migrate/not migrate all the eligible offers for a seller. <br><b style='color:green;'>Market
    availability: US</span></b>"""

    carrier_configs: Optional[list[CarrierConfig22]] = Field(default=UNSET, alias="carrierConfigs")
    """Defines the carrier configurations used for shipping, like carrier details and their corresponding region
    coverage. <br><b style='color:green;'>Market availability: US</span></b>"""


class AccountConfigs11Dict(TypedDict):
    shipping_priority: NotRequired[ShippingPriority7OrStr]
    migrate_eligible_offers: NotRequired[bool]
    carrier_configs: NotRequired[list[CarrierConfig22Dict]]
