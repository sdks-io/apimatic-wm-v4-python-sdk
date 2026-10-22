from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .carrier19 import Carrier19, Carrier19Dict
from .configuration18 import Configuration18, Configuration18Dict


class CarrierConfig22(SdkBaseModel):
    """Defines the carrier configurations used for shipping, like carrier details and their corresponding region
    coverage.."""

    configurations: Optional[list[Configuration18]] = UNSET
    """Defines the carrier configurations used for shipping, like carrier details and their corresponding region
    coverage. <br><b style='color:green;'>Market availability: US</span></b>"""

    carriers: Optional[list[Carrier19]] = UNSET
    """Defines the carrier configurations used for shipping, like carrier name and carrier service. <br><b
    style='color:green;'>Market availability: US</span></b>"""


class CarrierConfig22Dict(TypedDict):
    configurations: NotRequired[list[Configuration18Dict]]
    carriers: NotRequired[list[Carrier19Dict]]
