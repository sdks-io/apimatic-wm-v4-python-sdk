from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Quantity1(SdkBaseModel):
    """quantity.<br><b style='color:green;'>Market availability: MX</b>"""

    unit_of_measurement: Optional[str] = Field(default=UNSET, alias="unitOfMeasurement")
    """currency.<br><b style='color:green;'>Market availability: MX</b>"""

    amount: Optional[str] = UNSET
    """amount.<br><b style='color:green;'>Market availability: MX</b>"""


class Quantity1Dict(TypedDict):
    unit_of_measurement: NotRequired[str]
    amount: NotRequired[str]
