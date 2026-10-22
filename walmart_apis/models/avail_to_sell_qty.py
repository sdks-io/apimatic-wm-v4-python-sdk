from __future__ import annotations

from typing import Literal

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AvailToSellQty(SdkBaseModel):
    """Quantity of an item that is available to be allocated to orders."""

    unit: Literal["EACH"] = "EACH"
    """The unit of measurement. Example: 'EACH'"""

    amount: float
    """Inventory Count"""


class AvailToSellQtyDict(TypedDict):
    unit: Literal["EACH"]
    amount: float
