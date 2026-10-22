from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Price1(SdkBaseModel):
    """Competitor's item shipping price details of the item recommendation."""

    amount: Optional[float] = UNSET
    """The numerical amount of the price. Example: 9.99"""

    currency: Optional[str] = UNSET
    """Currency associated with the price of the item recommendation."""


class Price1Dict(TypedDict):
    amount: NotRequired[float]
    currency: NotRequired[str]
