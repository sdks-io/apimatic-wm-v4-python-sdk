from __future__ import annotations

from typing import Literal

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class InputQty(SdkBaseModel):
    """Quantity of an item that is input by the seller"""

    unit: Literal["EACH"] = "EACH"
    """The unit of measurement. Example: 'EACH'"""

    amount: float
    """Inventory Count"""


class InputQtyDict(TypedDict):
    unit: Literal["EACH"]
    amount: float
