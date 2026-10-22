from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .carrier_config16 import CarrierConfig16, CarrierConfig16Dict


class ShipNodeConfig5(SdkBaseModel):
    """Comprises a list of all fulfillment center IDs along with their respective configurations."""

    ship_nodes: Optional[list[str]] = Field(default=UNSET, alias="shipNodes")
    """List of Fulfillment Center Ids which are used as shipping nodes. <br><b style='color:green;'>Market availability:
    US</span></b>"""

    is_overridden: Optional[bool] = Field(default=UNSET, alias="isOverridden")
    """Flag denoting if the Fulfillment Center config settings are overriding account level settings. <br><b
    style='color:green;'>Market availability: US</span></b>"""

    carrier_configs: Optional[list[CarrierConfig16]] = Field(default=UNSET, alias="carrierConfigs")
    """List of Fulfillment Center Ids which are used as shipping nodes. <br><b style='color:green;'>Market availability:
    US</span></b>"""


class ShipNodeConfig5Dict(TypedDict):
    ship_nodes: NotRequired[list[str]]
    is_overridden: NotRequired[bool]
    carrier_configs: NotRequired[list[CarrierConfig16Dict]]
