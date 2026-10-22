from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .shipping_configuration import ShippingConfiguration, ShippingConfigurationDict


class Programs2(SdkBaseModel):
    """The type of shipping configuration to migrate."""

    shipping_configuration: Optional[ShippingConfiguration] = Field(default=UNSET, alias="shippingConfiguration")


class Programs2Dict(TypedDict):
    shipping_configuration: NotRequired[ShippingConfigurationDict]
