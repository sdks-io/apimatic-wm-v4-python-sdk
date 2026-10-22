from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .product_type2 import ProductType2, ProductType2Dict


class Payload16(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US only</b>"""

    name: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US only</b>"""

    count: Optional[int] = UNSET
    """<br><b style='color:green;'>Market availability: US only</b>"""

    product_type: Optional[list[ProductType2]] = Field(default=UNSET, alias="productType")
    """An array specifying different types of products. This field is only applicable for categories.<br><b
    style='color:green;'>Market availability: US only</b>"""


class Payload16Dict(TypedDict):
    name: NotRequired[str]
    count: NotRequired[int]
    product_type: NotRequired[list[ProductType2Dict]]
