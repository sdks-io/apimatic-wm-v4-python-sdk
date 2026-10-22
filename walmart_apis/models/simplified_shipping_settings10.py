from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_configs9 import AccountConfigs9, AccountConfigs9Dict


class SimplifiedShippingSettings10(SdkBaseModel):
    """Simplified Shipping Settings. <br><b style='color:green;'>Market availability: US</span></b>"""

    account_configs: Optional[AccountConfigs9] = Field(default=UNSET, alias="accountConfigs")
    """Account configuration to be set for a seller, comprising of Carrier configurations and Region configurations.
    <br><b style='color:green;'>Market availability: US</span></b>"""


class SimplifiedShippingSettings10Dict(TypedDict):
    account_configs: NotRequired[AccountConfigs9Dict]
