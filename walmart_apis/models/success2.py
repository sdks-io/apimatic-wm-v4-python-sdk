from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item10 import Item10, Item10Dict


class Success2(SdkBaseModel):
    """Items succeeded.<br><b style='color:green;'>Market availability: US only</b>"""

    items: Optional[list[Item10]] = UNSET
    """Items."""


class Success2Dict(TypedDict):
    items: NotRequired[list[Item10Dict]]
