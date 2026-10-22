from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ItemIdentifiers(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US</b>, Item Identifier which needs to be migrated., Item
    Identifier which needs to be migrated. <br><b style='color:green;'>Market availability: US</span></b>"""

    sku: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US</b>"""


class ItemIdentifiersDict(TypedDict):
    sku: NotRequired[str]
