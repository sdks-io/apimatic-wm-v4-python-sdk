from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Price8(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    amount: Optional[str] = UNSET
    """The numerical value of the price<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    currency: Optional[str] = UNSET
    """The currency type<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class Price8Dict(TypedDict):
    amount: NotRequired[str]
    currency: NotRequired[str]
