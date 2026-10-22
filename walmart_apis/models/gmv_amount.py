from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GmvAmount(SdkBaseModel):
    amount: Optional[int] = UNSET
    """The numerical value of the price"""

    currency: Optional[str] = UNSET
    """The currency type"""


class GmvAmountDict(TypedDict):
    amount: NotRequired[int]
    currency: NotRequired[str]
