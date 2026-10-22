from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .promo_discount import PromoDiscount, PromoDiscountDict


class PriceFeedPromoDiscountItem(SdkBaseModel):
    promo_discount: PromoDiscount = Field(alias="Promo&Discount")
    """The field ‘Promo&Discount’ is for the US market. <br><b style='color:green;'>Market availability: US</b>"""


class PriceFeedPromoDiscountItemDict(TypedDict):
    promo_discount: PromoDiscountDict
