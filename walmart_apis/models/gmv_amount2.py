from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GmvAmount2(SdkBaseModel):
    amount: Optional[int] = UNSET
    """The numerical value of the price<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    currency: Optional[str] = UNSET
    """The currency type<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class GmvAmount2Dict(TypedDict):
    amount: NotRequired[int]
    currency: NotRequired[str]
