from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .simplified_account_config_for_update_dto import (
    SimplifiedAccountConfigForUpdateDto,
    SimplifiedAccountConfigForUpdateDtoDict,
)


class SimplifiedAccountShippingSettingsForUpdateDto(SdkBaseModel):
    """Simplified Shipping Settings"""

    account_configs: Optional[SimplifiedAccountConfigForUpdateDto] = Field(default=UNSET, alias="accountConfigs")
    """Account configuration to be set for a seller, comprising of Carrier configurations and Region configurations."""


class SimplifiedAccountShippingSettingsForUpdateDtoDict(TypedDict):
    account_configs: NotRequired[SimplifiedAccountConfigForUpdateDtoDict]
