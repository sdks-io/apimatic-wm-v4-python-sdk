from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_configs7 import AccountConfigs7, AccountConfigs7Dict


class SimplifiedShippingSettings8(SdkBaseModel):
    """Simplified Shipping Settings. <br><b style='color:green;'>Market availability: US</span></b>"""

    account_configs: Optional[AccountConfigs7] = Field(default=UNSET, alias="accountConfigs")
    """Account configuration to be set for a seller, comprising of Carrier configurations and Region configurations.
    <br><b style='color:green;'>Market availability: US</span></b>"""


class SimplifiedShippingSettings8Dict(TypedDict):
    account_configs: NotRequired[AccountConfigs7Dict]
