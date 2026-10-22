from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .carrier_config18 import CarrierConfig18, CarrierConfig18Dict


class AccountConfigs7(SdkBaseModel):
    """Account configuration to be set for a seller, comprising of Carrier configurations and Region configurations.
    <br><b style='color:green;'>Market availability: US</span></b>"""

    migrate_eligible_offers: Optional[bool] = Field(default=UNSET, alias="migrateEligibleOffers")
    """Flag used to migrate/not migrate all the eligible offers for a seller. <br><b style='color:green;'>Market
    availability: US</span></b>"""

    carrier_configs: Optional[list[CarrierConfig18]] = Field(default=UNSET, alias="carrierConfigs")
    """Defines the carrier configurations used for shipping, like carrier details and their corresponding region
    coverage.. <br><b style='color:green;'>Market availability: US</span></b>"""


class AccountConfigs7Dict(TypedDict):
    migrate_eligible_offers: NotRequired[bool]
    carrier_configs: NotRequired[list[CarrierConfig18Dict]]
