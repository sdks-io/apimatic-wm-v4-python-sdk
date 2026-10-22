from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Price22(SdkBaseModel):
    """Price range of the items.<br><b style='color:green;'>Market availability: US only</b>"""

    minimum: Optional[float] = UNSET
    """Minimum price of the item.<br><b style='color:green;'>Market availability: US only</b>"""

    maximum: Optional[float] = UNSET
    """Maximum price of the item.<br><b style='color:green;'>Market availability: US only</b>"""


class Price22Dict(TypedDict):
    minimum: NotRequired[float]
    maximum: NotRequired[float]
