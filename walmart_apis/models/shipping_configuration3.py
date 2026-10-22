from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ShippingConfiguration3(SdkBaseModel):
    """Defines the shipping configuration settings for the SKU. <br><b style='color:green;'>Market availability:
    US</span></b>"""

    item_shipping_configuration: Optional[str] = Field(default=UNSET, alias="itemShippingConfiguration")
    """Specifies the type of shipping configuration to which the current SKU should be migrated. Eligible values for
    this field are: Simplified Shipping Settings and Manual Template. <br><b style='color:green;'>Market availability:
    US</span></b>"""


class ShippingConfiguration3Dict(TypedDict):
    item_shipping_configuration: NotRequired[str]
