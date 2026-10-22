from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.field42 import Field42OrStr


class Search1(SdkBaseModel):
    """Search request.<br><b style='color:green;'>Market availability: US only</b>"""

    field: Optional[Field42OrStr] = UNSET
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ITEM_NAME | Product name | string |
    | SKU | Specifies the item identified. This value is defined by the seller. | string |
    <br><b style='color:green;'>Market availability: US only</b>"""

    value: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US only</b>"""


class Search1Dict(TypedDict):
    field: NotRequired[Field42OrStr]
    value: NotRequired[str]
