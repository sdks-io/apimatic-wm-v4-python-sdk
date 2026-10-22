from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .shipping_configuration3 import ShippingConfiguration3, ShippingConfiguration3Dict


class Programs21(SdkBaseModel):
    """The type of shipping configuration to migrate. <br><b style='color:green;'>Market availability: US</span></b>"""

    shipping_configuration: Optional[ShippingConfiguration3] = Field(default=UNSET, alias="shippingConfiguration")
    """Defines the shipping configuration settings for the SKU. <br><b style='color:green;'>Market availability:
    US</span></b>"""


class Programs21Dict(TypedDict):
    shipping_configuration: NotRequired[ShippingConfiguration3Dict]
