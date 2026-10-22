from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .gmv4 import Gmv4, Gmv4Dict


class Stats2(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    gmv: Optional[Gmv4] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    page_views: Optional[str] = Field(default=UNSET, alias="pageViews")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    orders: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    conversion_rate: Optional[str] = Field(default=UNSET, alias="conversionRate")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    total_units: Optional[str] = Field(default=UNSET, alias="totalUnits")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class Stats2Dict(TypedDict):
    gmv: NotRequired[Gmv4Dict]
    page_views: NotRequired[str]
    orders: NotRequired[str]
    conversion_rate: NotRequired[str]
    total_units: NotRequired[str]
