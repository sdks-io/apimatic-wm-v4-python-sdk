from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ItemPrice11(SdkBaseModel):
    """Competitor's item shipping price details of the item recommendation. <br><b style='color:green;'>Market
    availability: US | CA | MX</span></b>"""

    amount: Optional[float] = UNSET
    """The numerical amount of the price. Example: 9.99 <br><b style='color:green;'>Market availability: US |
    CA</span></b>"""

    currency: Optional[str] = UNSET
    """Currency associated with the price of the item recommendation. <br><b style='color:green;'>Market availability:
    US | CA | MX</span></b>"""


class ItemPrice11Dict(TypedDict):
    amount: NotRequired[float]
    currency: NotRequired[str]
