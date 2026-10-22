from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ShippingConfiguration(SdkBaseModel):
    item_shipping_configuration: Optional[str] = Field(default=UNSET, alias="itemShippingConfiguration")
    """Type of shipping configuration to where current SKU should be migrated to. Eligible values for the field are:
    Simplified Shipping Settings & Manual Template"""


class ShippingConfigurationDict(TypedDict):
    item_shipping_configuration: NotRequired[str]
