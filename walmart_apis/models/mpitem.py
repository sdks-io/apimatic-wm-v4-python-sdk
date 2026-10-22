from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .price11 import Price11, Price11Dict


class Mpitem(SdkBaseModel):
    price: Optional[Price11] = Field(default=UNSET, alias="Price")
    """Applicable for CA, MX, and CL markets. Price details for the item. <br><b style='color:green;'>Market
    availability: CA | MX | CL</b>"""


class MpitemDict(TypedDict):
    price: NotRequired[Price11Dict]
