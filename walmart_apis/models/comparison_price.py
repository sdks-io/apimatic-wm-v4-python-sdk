from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.currency import CurrencyOrStr


class ComparisonPrice(SdkBaseModel):
    """This is applicable only for promotions, Charge of AddOn type., Declared value of shipment. This value is
    applicable in case of INSURANCE AddOn Type only., Charge of add-on type., Declared value of shipment. This value is
    applicable in case of INSURANCE add-on type only."""

    currency: Optional[CurrencyOrStr] = UNSET
    amount: Optional[float] = UNSET


class ComparisonPriceDict(TypedDict):
    currency: NotRequired[CurrencyOrStr]
    amount: NotRequired[float]
