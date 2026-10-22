from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MaxSalesRetailPrice2(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: Global</b>"""

    value: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: Global</b>"""

    currency: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: Global</b>"""

    amount: Optional[float] = UNSET
    """<br><b style='color:green;'>Market availability: Global</b>"""


class MaxSalesRetailPrice2Dict(TypedDict):
    value: NotRequired[str]
    currency: NotRequired[str]
    amount: NotRequired[float]
