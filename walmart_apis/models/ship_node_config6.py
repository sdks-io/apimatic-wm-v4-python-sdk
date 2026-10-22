from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .carrier_config17 import CarrierConfig17, CarrierConfig17Dict


class ShipNodeConfig6(SdkBaseModel):
    """Comprises a list of all fulfillment center IDs along with their respective configurations."""

    ship_nodes: Optional[list[str]] = Field(default=UNSET, alias="shipNodes")
    """List of Fulfillment Center Ids which are used as shipping nodes. <br><b style='color:green;'>Market availability:
    US</span></b>"""

    is_overridden: Optional[bool] = Field(default=UNSET, alias="isOverridden")
    """Flag denoting if the Fulfillment Center config settings are overriding account level settings. <br><b
    style='color:green;'>Market availability: US</span></b>"""

    carrier_configs: Optional[list[CarrierConfig17]] = Field(default=UNSET, alias="carrierConfigs")
    """List of Fulfillment Center Ids which are used as shipping nodes. <br><b style='color:green;'>Market availability:
    US</span></b>"""


class ShipNodeConfig6Dict(TypedDict):
    ship_nodes: NotRequired[list[str]]
    is_overridden: NotRequired[bool]
    carrier_configs: NotRequired[list[CarrierConfig17Dict]]
