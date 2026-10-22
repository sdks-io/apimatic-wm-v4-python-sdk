from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Gmv4(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    amount: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    currency: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class Gmv4Dict(TypedDict):
    amount: NotRequired[str]
    currency: NotRequired[str]
