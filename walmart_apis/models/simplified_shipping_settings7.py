from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .ship_node_config6 import ShipNodeConfig6, ShipNodeConfig6Dict


class SimplifiedShippingSettings7(SdkBaseModel):
    """Simplified Shipping Settings. <br><b style='color:green;'>Market availability: US</span></b>"""

    ship_node_configs: Optional[list[ShipNodeConfig6]] = Field(default=UNSET, alias="shipNodeConfigs")
    """Comprises a list of all fulfillment center IDs along with their respective configurations. <br><b
    style='color:green;'>Market availability: US</span></b>"""


class SimplifiedShippingSettings7Dict(TypedDict):
    ship_node_configs: NotRequired[list[ShipNodeConfig6Dict]]
