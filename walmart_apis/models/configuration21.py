from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.address_type import AddressTypeOrStr
from .region22 import Region22, Region22Dict


class Configuration21(SdkBaseModel):
    """Defines the carrier configurations used for shipping, like carrier details and their corresponding region
    coverage.."""

    regions: Optional[list[Region22]] = UNSET
    """Region configurations to which shipping has to be covered with added carriers. <br><b style='color:green;'>Market
    availability: US</span></b>"""

    address_types: Optional[list[AddressTypeOrStr]] = Field(default=UNSET, alias="addressTypes")
    """Type of address to which shipping has to be covered as part of mentioned region, sub region and states. <br><b
    style='color:green;'>Market availability: US</span></b>"""


class Configuration21Dict(TypedDict):
    regions: NotRequired[list[Region22Dict]]
    address_types: NotRequired[list[AddressTypeOrStr]]
