from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fcconfig_dto import FcconfigDto, FcconfigDtoDict


class SimplifiedFcshippingSettingsDto(SdkBaseModel):
    """Simplified Shipping Settings"""

    ship_node_configs: Optional[list[FcconfigDto]] = Field(default=UNSET, alias="shipNodeConfigs")
    """Comprises a list of all fulfillment center IDs along with their respective configurations."""


class SimplifiedFcshippingSettingsDtoDict(TypedDict):
    ship_node_configs: NotRequired[list[FcconfigDtoDict]]
