from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .promotion_information import PromotionInformation, PromotionInformationDict


class Price12(SdkBaseModel):
    """Applicable for CA, MX, and CL markets. Price details for the item. <br><b style='color:green;'>Market
    availability: CA | MX | CL</b>"""

    sku: str
    """The SKU of the item for which the promotion is being updated.<br><b style='color:green;'>Market availability: CA
    | MX | CL </b>"""

    price: float
    """The current selling price of the item on Walmart.com.<br><b style='color:green;'>Market availability: CA | MX |
    CL </b>"""

    msrp: Optional[float] = UNSET
    """The manufacturer's suggested retail price (MSRP) for the item.<br><b style='color:green;'>Market availability: CA
    | MX | CL</b>"""

    promotion_information: Optional[PromotionInformation] = Field(default=UNSET, alias="promotionInformation")


class Price12Dict(TypedDict):
    sku: str
    price: float
    msrp: NotRequired[float]
    promotion_information: NotRequired[PromotionInformationDict]
