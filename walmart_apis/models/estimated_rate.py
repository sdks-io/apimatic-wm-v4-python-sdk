from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.currency8 import Currency8OrStr


class EstimatedRate(SdkBaseModel):
    """Estimated Rate"""

    amount: Optional[float] = UNSET
    currency: Optional[Currency8OrStr] = UNSET


class EstimatedRateDict(TypedDict):
    amount: NotRequired[float]
    currency: NotRequired[Currency8OrStr]
