from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .price4 import Price4, Price4Dict


class PriceFeedPriceItem(SdkBaseModel):
    price: Price4 = Field(alias="Price")
    """Applicable for CA, MX, and CL markets. Price details for the item.<br><b style='color:green;'>Market
    availability: CA | MX | CL</b>"""


class PriceFeedPriceItemDict(TypedDict):
    price: Price4Dict
