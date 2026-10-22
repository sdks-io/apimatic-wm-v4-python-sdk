from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .carrier_config_dto import CarrierConfigDto, CarrierConfigDtoDict


class FcconfigDto(SdkBaseModel):
    """Comprises a list of all fulfillment center IDs along with their respective configurations."""

    ship_nodes: Optional[list[str]] = Field(default=UNSET, alias="shipNodes")
    """List of Fulfillment Center Ids which are used as shipping nodes."""

    is_overridden: Optional[bool] = Field(default=UNSET, alias="isOverridden")
    """Flag denoting if the Fulfillment Center config settings are overriding account level settings"""

    carrier_configs: Optional[list[CarrierConfigDto]] = Field(default=UNSET, alias="carrierConfigs")
    """List of Fulfillment Center Ids which are used as shipping nodes."""


class FcconfigDtoDict(TypedDict):
    ship_nodes: NotRequired[list[str]]
    is_overridden: NotRequired[bool]
    carrier_configs: NotRequired[list[CarrierConfigDtoDict]]
