from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .state23 import State23, State23Dict


class SubRegion22(SdkBaseModel):
    """Sub region configurations to which shipping has to be covered with added carriers. <br><b
    style='color:green;'>Market availability: US</span></b>"""

    sub_region_code: Optional[str] = Field(default=UNSET, alias="subRegionCode")
    """Sub region code for covered shipping. <br><b style='color:green;'>Market availability: US</span></b>"""

    sub_region_name: Optional[str] = Field(default=UNSET, alias="subRegionName")
    """Sub region name for covered shipping. <br><b style='color:green;'>Market availability: US</span></b>"""

    states: Optional[list[State23]] = UNSET
    """State configuration to which shipping has to be covered with added carriers as part of mentioned sub region area.
    <br><b style='color:green;'>Market availability: US</span></b>"""


class SubRegion22Dict(TypedDict):
    sub_region_code: NotRequired[str]
    sub_region_name: NotRequired[str]
    states: NotRequired[list[State23Dict]]
