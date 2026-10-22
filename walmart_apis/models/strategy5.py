from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Strategy5(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    sku: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    repricer_strategy: Optional[str] = Field(default=UNSET, alias="repricerStrategy")
    """Specifies the name of the strategy collection. This value is used to group and manage related repricing
    strategies.<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    minimum_seller_allowed_price: Optional[float] = Field(default=UNSET, alias="minimumSellerAllowedPrice")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    maximum_seller_allowed_price: Optional[float] = Field(default=UNSET, alias="maximumSellerAllowedPrice")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class Strategy5Dict(TypedDict):
    sku: NotRequired[str]
    repricer_strategy: NotRequired[str]
    minimum_seller_allowed_price: NotRequired[float]
    maximum_seller_allowed_price: NotRequired[float]
