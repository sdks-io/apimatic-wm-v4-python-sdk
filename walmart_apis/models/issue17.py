from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Issue17(SdkBaseModel):
    title: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    value: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class Issue17Dict(TypedDict):
    title: NotRequired[str]
    value: NotRequired[str]
