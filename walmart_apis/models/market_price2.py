from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MarketPrice2(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    amount: Optional[str] = UNSET
    """The numerical value of the price<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    currency: Optional[str] = UNSET
    """The currency type<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class MarketPrice2Dict(TypedDict):
    amount: NotRequired[str]
    currency: NotRequired[str]
