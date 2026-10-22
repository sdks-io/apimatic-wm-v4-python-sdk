from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item111 import Item111, Item111Dict


class Failure2(SdkBaseModel):
    """Items failed.<br><b style='color:green;'>Market availability: US only</b>"""

    items: Optional[list[Item111]] = UNSET
    """Items."""


class Failure2Dict(TypedDict):
    items: NotRequired[list[Item111Dict]]
