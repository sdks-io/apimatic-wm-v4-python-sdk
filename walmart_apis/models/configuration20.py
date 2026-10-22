from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.address_type import AddressTypeOrStr
from .region21 import Region21, Region21Dict


class Configuration20(SdkBaseModel):
    """Defines the carrier configurations used for shipping, like carrier details and their corresponding region
    coverage.."""

    regions: Optional[list[Region21]] = UNSET
    """Region configurations to which shipping has to be covered with added carriers. <br><b style='color:green;'>Market
    availability: US</span></b>"""

    address_types: Optional[list[AddressTypeOrStr]] = Field(default=UNSET, alias="addressTypes")
    """Type of address to which shipping has to be covered as part of mentioned region, sub region and states. <br><b
    style='color:green;'>Market availability: US</span></b>"""


class Configuration20Dict(TypedDict):
    regions: NotRequired[list[Region21Dict]]
    address_types: NotRequired[list[AddressTypeOrStr]]
