from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sub_region20 import SubRegion20, SubRegion20Dict


class Region19(SdkBaseModel):
    """Region configurations to which shipping has to be covered with added carriers."""

    region_code: Optional[str] = Field(default=UNSET, alias="regionCode")
    """Region code for covered shipping. <br><b style='color:green;'>Market availability: US</span></b>"""

    region_name: Optional[str] = Field(default=UNSET, alias="regionName")
    """Region name for covered shipping. <br><b style='color:green;'>Market availability: US</span></b>"""

    sub_regions: Optional[list[SubRegion20]] = Field(default=UNSET, alias="subRegions")
    """Sub region configurations to which shipping has to be covered with added carriers. <br><b
    style='color:green;'>Market availability: US</span></b>"""


class Region19Dict(TypedDict):
    region_code: NotRequired[str]
    region_name: NotRequired[str]
    sub_regions: NotRequired[list[SubRegion20Dict]]
