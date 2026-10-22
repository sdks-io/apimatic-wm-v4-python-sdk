from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.address_type import AddressTypeOrStr
from .region19 import Region19, Region19Dict


class Configuration18(SdkBaseModel):
    """Defines the carrier configurations used for shipping, like carrier details and their corresponding region
    coverage.."""

    regions: Optional[list[Region19]] = UNSET
    """Region configurations to which shipping has to be covered with added carriers. <br><b style='color:green;'>Market
    availability: US</span></b>"""

    address_types: Optional[list[AddressTypeOrStr]] = Field(default=UNSET, alias="addressTypes")
    """Type of address to which shipping has to be covered as part of mentioned region, sub region and states. <br><b
    style='color:green;'>Market availability: US</span></b>"""


class Configuration18Dict(TypedDict):
    regions: NotRequired[list[Region19Dict]]
    address_types: NotRequired[list[AddressTypeOrStr]]
