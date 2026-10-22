from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MoneyType(SdkBaseModel):
    value: Optional[str] = UNSET
    currency: Optional[str] = UNSET
    amount: Optional[float] = UNSET


class MoneyTypeDict(TypedDict):
    value: NotRequired[str]
    currency: NotRequired[str]
    amount: NotRequired[float]
