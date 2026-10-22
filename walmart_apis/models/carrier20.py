from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Carrier20(SdkBaseModel):
    """Defines the carrier configurations used for shipping, like carrier name and carrier service."""

    carrier_name: Optional[str] = Field(default=UNSET, alias="carrierName")
    """Name of the carrier to use for shipping. <br><b style='color:green;'>Market availability: US</span></b>"""

    carrier_service: Optional[str] = Field(default=UNSET, alias="carrierService")
    """Defines the carrier configurations used for shipping, like carrier name and carrier service. <br><b
    style='color:green;'>Market availability: US</span></b>"""


class Carrier20Dict(TypedDict):
    carrier_name: NotRequired[str]
    carrier_service: NotRequired[str]
