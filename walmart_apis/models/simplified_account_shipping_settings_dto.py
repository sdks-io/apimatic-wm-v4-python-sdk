from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .simplified_account_config_dto import SimplifiedAccountConfigDto, SimplifiedAccountConfigDtoDict


class SimplifiedAccountShippingSettingsDto(SdkBaseModel):
    """Simplified Shipping Settings"""

    account_configs: Optional[SimplifiedAccountConfigDto] = Field(default=UNSET, alias="accountConfigs")
    """Account configuration to be set for a seller, comprising of Carrier configurations and Region configurations."""


class SimplifiedAccountShippingSettingsDtoDict(TypedDict):
    account_configs: NotRequired[SimplifiedAccountConfigDtoDict]
