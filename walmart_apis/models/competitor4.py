from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_price11 import ItemPrice11, ItemPrice11Dict
from .shipping_price10 import ShippingPrice10, ShippingPrice10Dict


class Competitor4(SdkBaseModel):
    """Competitor's item information."""

    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    """Competitor item ID. <br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""

    url: Optional[str] = UNSET
    """Competitor item URL. <br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""

    item_price: Optional[ItemPrice11] = Field(default=UNSET, alias="itemPrice")
    """Competitor's item shipping price details of the item recommendation. <br><b style='color:green;'>Market
    availability: US | CA | MX</span></b>"""

    shipping_price: Optional[ShippingPrice10] = Field(default=UNSET, alias="shippingPrice")
    """Competitor's item shipping price details of the item recommendation. <br><b style='color:green;'>Market
    availability: US | CA | MX</span></b>"""


class Competitor4Dict(TypedDict):
    item_id: NotRequired[str]
    url: NotRequired[str]
    item_price: NotRequired[ItemPrice11Dict]
    shipping_price: NotRequired[ShippingPrice10Dict]
