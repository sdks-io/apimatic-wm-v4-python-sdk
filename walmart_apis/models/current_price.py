from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.currency import CurrencyOrStr


class CurrentPrice(SdkBaseModel):
    currency: Optional[CurrencyOrStr] = UNSET
    amount: Optional[float] = UNSET


class CurrentPriceDict(TypedDict):
    currency: NotRequired[CurrencyOrStr]
    amount: NotRequired[float]
