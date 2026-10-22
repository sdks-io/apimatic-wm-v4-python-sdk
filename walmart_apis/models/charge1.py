from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .gmv import Gmv, GmvDict
from .tax1 import Tax1, Tax1Dict


class Charge1(SdkBaseModel):
    charge_type: Optional[str] = Field(default=UNSET, alias="chargeType")
    """chargeType.<br><b style='color:green;'>Market availability: MX</b>"""

    charge_name: Optional[str] = Field(default=UNSET, alias="chargeName")
    """chargeName.<br><b style='color:green;'>Market availability: Global</b>"""

    charge_amount: Optional[Gmv] = Field(default=UNSET, alias="chargeAmount")
    """chargeAmount.<br><b style='color:green;'>Market availability: MX | CA |CL</b>"""

    tax: Optional[list[Tax1]] = UNSET
    """tax.<br><b style='color:green;'>Market availability: MX</b>"""


class Charge1Dict(TypedDict):
    charge_type: NotRequired[str]
    charge_name: NotRequired[str]
    charge_amount: NotRequired[GmvDict]
    tax: NotRequired[list[Tax1Dict]]
