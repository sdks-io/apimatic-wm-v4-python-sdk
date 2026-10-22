from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PromoDiscount(SdkBaseModel):
    """The field ‘Promo&Discount’ is for the US market. <br><b style='color:green;'>Market availability: US</b>"""

    sku: str
    """The SKU of the item for which the price is being updated.<br><b style='color:green;'>Market availability:
    US</b>"""

    price: float
    """The current selling price of the item on Walmart.com.<br><b style='color:green;'>Market availability: US</b>"""

    msrp: Optional[float] = UNSET
    """The manufacturer's suggested retail price (MSRP) for the item.<br><b style='color:green;'>Market availability:
    US</b>"""


class PromoDiscountDict(TypedDict):
    sku: str
    price: float
    msrp: NotRequired[float]
