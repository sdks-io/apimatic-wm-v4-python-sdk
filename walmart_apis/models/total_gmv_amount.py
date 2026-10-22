from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TotalGmvAmount(SdkBaseModel):
    """Gross Merchandise Value of the total result set"""

    amount: Optional[str] = UNSET
    """The numerical value of the price"""

    currency: Optional[str] = UNSET
    """The currency type"""


class TotalGmvAmountDict(TypedDict):
    amount: NotRequired[str]
    currency: NotRequired[str]
