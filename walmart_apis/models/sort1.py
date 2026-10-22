from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.field51 import Field51OrStr
from .enums.order import OrderOrStr


class Sort1(SdkBaseModel):
    """Sort request.<br><b style='color:green;'>Market availability: US only</b>"""

    field: Optional[Field51OrStr] = UNSET
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ITEM_PRIORITY | Recommended priority of the item by Walmart. | integer |
    | PRICE | Item price | integer |
    <br><b style='color:green;'>Market availability: US only</b>"""

    order: Optional[OrderOrStr] = UNSET
    """<br><b style='color:green;'>Market availability: US only</b>"""

    priority: Optional[int] = UNSET
    """Sort priority of the specified field.<br><b style='color:green;'>Market availability: US only</b>"""


class Sort1Dict(TypedDict):
    field: NotRequired[Field51OrStr]
    order: NotRequired[OrderOrStr]
    priority: NotRequired[int]
