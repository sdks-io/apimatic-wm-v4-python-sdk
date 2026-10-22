from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PriceRequest(SdkBaseModel):
    """Price range of the items."""

    minimum: Optional[float] = UNSET
    """Minimum price of the item."""

    maximum: Optional[float] = UNSET
    """Maximum price of the item."""


class PriceRequestDict(TypedDict):
    minimum: NotRequired[float]
    maximum: NotRequired[float]
