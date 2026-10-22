from __future__ import annotations

from typing import Literal

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class InputQty13(SdkBaseModel):
    """Indicates the quantity that has been ordered by the customers but not yet shipped.

    <strong style="color: green;">Market availability: Global</strong>"""

    unit: Literal["EACH"] = "EACH"
    """Indicates a unit of measure. Walmart Marketplace supports only EACH, which indicates one individual sellable
    item.

    <strong style="color: green;">Market availability: Global</strong>"""

    amount: float
    """Inventory Count.

    <strong style="color: green;">Market availability: Global</strong>"""


class InputQty13Dict(TypedDict):
    unit: Literal["EACH"]
    amount: float
