from __future__ import annotations

from typing import Literal

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ReservedQty(SdkBaseModel):
    """Quantity that has been ordered by the customers but not yet shipped."""

    unit: Literal["EACH"] = "EACH"
    """The unit of measurement. Example: 'EACH'"""

    amount: float
    """Inventory Count"""


class ReservedQtyDict(TypedDict):
    unit: Literal["EACH"]
    amount: float
