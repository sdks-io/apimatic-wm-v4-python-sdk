from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .promotion_information1 import PromotionInformation1, PromotionInformation1Dict


class PromoDiscount1(SdkBaseModel):
    """The field ‘Promo&Discount’ is for the US market. <br><b style='color:green;'>Market availability: US</b>"""

    sku: str
    """The SKU of the item for which the promotion is being updated.<br><b style='color:green;'>Market availability:
    US</b>"""

    price: float
    """The current selling price of the item on Walmart.com.<br><b style='color:green;'>Market availability: US</b>"""

    msrp: Optional[float] = UNSET
    """The manufacturer's suggested retail price (MSRP) for the item.<br><b style='color:green;'>Market availability:
    US</b>"""

    promoid: Optional[str] = UNSET
    """Promotion ID is required to update the existing promotion information. <br><b style='color:green;'>Market
    availability: US"""

    promotion_information: Optional[PromotionInformation1] = Field(default=UNSET, alias="promotionInformation")


class PromoDiscount1Dict(TypedDict):
    sku: str
    price: float
    msrp: NotRequired[float]
    promoid: NotRequired[str]
    promotion_information: NotRequired[PromotionInformation1Dict]
