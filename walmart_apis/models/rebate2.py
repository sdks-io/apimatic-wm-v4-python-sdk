from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.rebate_type3 import RebateType3OrStr
from .rebate_amt3 import RebateAmt3, RebateAmt3Dict


class Rebate2(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: Global</b>"""

    rebate_amt: RebateAmt3 = Field(alias="rebateAmt")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    info_url: Optional[str] = Field(default=UNSET, alias="infoUrl")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    rebate_type: Optional[RebateType3OrStr] = Field(default=UNSET, alias="rebateType")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    start_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="startDate")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    end_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="endDate")
    """<br><b style='color:green;'>Market availability: Global</b>"""


class Rebate2Dict(TypedDict):
    rebate_amt: RebateAmt3Dict
    info_url: NotRequired[str]
    rebate_type: NotRequired[RebateType3OrStr]
    start_date: NotRequired[RFC3339DateTime]
    end_date: NotRequired[RFC3339DateTime]
