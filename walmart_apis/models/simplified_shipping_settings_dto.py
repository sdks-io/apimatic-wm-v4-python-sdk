from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fcconfig_dto import FcconfigDto, FcconfigDtoDict
from .simplified_account_config_for_get_dto import (
    SimplifiedAccountConfigForGetDto,
    SimplifiedAccountConfigForGetDtoDict,
)


class SimplifiedShippingSettingsDto(SdkBaseModel):
    """Simplified Shipping Settings"""

    account_configs: Optional[SimplifiedAccountConfigForGetDto] = Field(default=UNSET, alias="accountConfigs")
    """Account configuration to be set for a seller, comprising of Carrier configurations and Region configurations."""

    ship_node_configs: Optional[list[FcconfigDto]] = Field(default=UNSET, alias="shipNodeConfigs")
    """Comprises a list of all fulfillment center IDs along with their respective configurations."""


class SimplifiedShippingSettingsDtoDict(TypedDict):
    account_configs: NotRequired[SimplifiedAccountConfigForGetDtoDict]
    ship_node_configs: NotRequired[list[FcconfigDtoDict]]
