from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_configs11 import AccountConfigs11, AccountConfigs11Dict
from .ship_node_config6 import ShipNodeConfig6, ShipNodeConfig6Dict


class SimplifiedShippingSettings12(SdkBaseModel):
    """Simplified Shipping Settings. <br><b style='color:green;'>Market availability: US</span></b>"""

    account_configs: Optional[AccountConfigs11] = Field(default=UNSET, alias="accountConfigs")
    """Account configuration to be set for a seller, comprising of Carrier configurations and Region configurations.
    <br><b style='color:green;'>Market availability: US</span></b>"""

    ship_node_configs: Optional[list[ShipNodeConfig6]] = Field(default=UNSET, alias="shipNodeConfigs")
    """Comprises a list of all fulfillment center IDs along with their respective configurations. <br><b
    style='color:green;'>Market availability: US</span></b>"""


class SimplifiedShippingSettings12Dict(TypedDict):
    account_configs: NotRequired[AccountConfigs11Dict]
    ship_node_configs: NotRequired[list[ShipNodeConfig6Dict]]
