from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ChargePerUnit(SdkBaseModel):
    """Price of One unit of item, in this order line.<br><b style='color:green;'>Market availability:US</b>"""

    currency_amount: Optional[float] = Field(default=UNSET, alias="currencyAmount")
    """Amount to be refunded..<br><b style='color:green;'>Market availability: US</b>"""

    currency_unit: Optional[str] = Field(default=UNSET, alias="currencyUnit")
    """Currency information.<br><b style='color:green;'>Market availability: US</b>"""


class ChargePerUnitDict(TypedDict):
    currency_amount: NotRequired[float]
    currency_unit: NotRequired[str]
