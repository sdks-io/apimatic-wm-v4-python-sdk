from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .state21 import State21, State21Dict


class SubRegion20(SdkBaseModel):
    """Sub region configurations to which shipping has to be covered with added carriers."""

    sub_region_code: Optional[str] = Field(default=UNSET, alias="subRegionCode")
    """Sub region code for covered shipping. <br><b style='color:green;'>Market availability: US</span></b>"""

    sub_region_name: Optional[str] = Field(default=UNSET, alias="subRegionName")
    """Sub region name for covered shipping. <br><b style='color:green;'>Market availability: US</span></b>"""

    states: Optional[list[State21]] = UNSET
    """State configuration to which shipping has to be covered with added carriers as part of mentioned sub region area.
    <br><b style='color:green;'>Market availability: US</span></b>"""


class SubRegion20Dict(TypedDict):
    sub_region_code: NotRequired[str]
    sub_region_name: NotRequired[str]
    states: NotRequired[list[State21Dict]]
