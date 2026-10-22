from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .price21 import Price21, Price21Dict


class Mpitem1(SdkBaseModel):
    price: Optional[Price21] = Field(default=UNSET, alias="Price")
    """Applicable for CA, MX, and CL markets. Price details for the item. <br><b style='color:green;'>Market
    availability: CA | MX | CL</b>"""


class Mpitem1Dict(TypedDict):
    price: NotRequired[Price21Dict]
