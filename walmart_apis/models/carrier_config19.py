from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .carrier19 import Carrier19, Carrier19Dict
from .configuration21 import Configuration21, Configuration21Dict


class CarrierConfig19(SdkBaseModel):
    """List of Fulfillment Center Ids which are used as shipping nodes."""

    is_default: Optional[bool] = Field(default=UNSET, alias="isDefault")
    """Indicates whether this configuration is set as the default for the fulfillment center. <br><b
    style='color:green;'>Market availability: US</span></b>"""

    configurations: Optional[list[Configuration21]] = UNSET
    """Defines the carrier configurations used for shipping, like carrier details and their corresponding region
    coverage. <br><b style='color:green;'>Market availability: US</span></b>"""

    carriers: Optional[list[Carrier19]] = UNSET
    """Defines the carrier configurations used for shipping, like carrier name and carrier service. <br><b
    style='color:green;'>Market availability: US</span></b>"""


class CarrierConfig19Dict(TypedDict):
    is_default: NotRequired[bool]
    configurations: NotRequired[list[Configuration21Dict]]
    carriers: NotRequired[list[Carrier19Dict]]
