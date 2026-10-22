from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MarketPrice(SdkBaseModel):
    amount: Optional[str] = UNSET
    """The numerical value of the price"""

    currency: Optional[str] = UNSET
    """The currency type"""


class MarketPriceDict(TypedDict):
    amount: NotRequired[str]
    currency: NotRequired[str]
