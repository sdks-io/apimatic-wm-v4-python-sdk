from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .price12 import Price12, Price12Dict


class PromotionFeedPriceItem(SdkBaseModel):
    price: Price12 = Field(alias="Price")
    """Applicable for CA, MX, and CL markets. Price details for the item. <br><b style='color:green;'>Market
    availability: CA | MX | CL</b>"""


class PromotionFeedPriceItemDict(TypedDict):
    price: Price12Dict
