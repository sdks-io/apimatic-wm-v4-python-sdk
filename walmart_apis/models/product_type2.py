from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ProductType2(SdkBaseModel):
    """The productType is only applicable for categories.<br><b style='color:green;'>Market availability: US only</b>"""

    name: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US only</b>"""

    count: Optional[int] = UNSET
    """<br><b style='color:green;'>Market availability: US only</b>"""


class ProductType2Dict(TypedDict):
    name: NotRequired[str]
    count: NotRequired[int]
