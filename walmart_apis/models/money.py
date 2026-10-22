from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.currency17 import Currency17OrStr


class Money(SdkBaseModel):
    """Estimated Rate"""

    amount: Optional[float] = UNSET
    """Monetary amount expressed as a decimal number."""

    currency: Optional[Currency17OrStr] = UNSET
    """Three-letter currency code (example, USD, MXN, CAD)."""


class MoneyDict(TypedDict):
    amount: NotRequired[float]
    currency: NotRequired[Currency17OrStr]
