from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Item12(SdkBaseModel):
    """item.<br><b style='color:green;'>Market availability: MX</b>"""

    product_name: Optional[str] = Field(default=UNSET, alias="productName")
    """productName.<br><b style='color:green;'>Market availability: MX</b>"""


class Item12Dict(TypedDict):
    product_name: NotRequired[str]
