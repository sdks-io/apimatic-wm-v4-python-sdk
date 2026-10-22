from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_configs10 import AccountConfigs10, AccountConfigs10Dict


class SimplifiedShippingSettings11(SdkBaseModel):
    """Simplified Shipping Settings. <br><b style='color:green;'>Market availability: US</span></b>"""

    account_configs: Optional[AccountConfigs10] = Field(default=UNSET, alias="accountConfigs")
    """Account configuration to be set for a seller, comprising of Carrier configurations and Region configurations.
    <br><b style='color:green;'>Market availability: US</span></b>"""


class SimplifiedShippingSettings11Dict(TypedDict):
    account_configs: NotRequired[AccountConfigs10Dict]
