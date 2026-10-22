from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_price10 import ItemPrice10, ItemPrice10Dict
from .shipping_price10 import ShippingPrice10, ShippingPrice10Dict


class Walmart4(SdkBaseModel):
    """Walmart's item information. <br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""

    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    """Walmart item ID. <br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""

    url: Optional[str] = UNSET
    """Walmart item URL. <br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""

    wfs_indicator: Optional[bool] = Field(default=UNSET, alias="wfsIndicator")
    """Walmart fulfilment service indicator. <br><b style='color:green;'>Market availability: US only</span></b>"""

    item_price: Optional[ItemPrice10] = Field(default=UNSET, alias="itemPrice")
    """Competitor's item shipping price details of the item recommendation."""

    shipping_price: Optional[ShippingPrice10] = Field(default=UNSET, alias="shippingPrice")
    """Competitor's item shipping price details of the item recommendation. <br><b style='color:green;'>Market
    availability: US | CA | MX</span></b>"""


class Walmart4Dict(TypedDict):
    item_id: NotRequired[str]
    url: NotRequired[str]
    wfs_indicator: NotRequired[bool]
    item_price: NotRequired[ItemPrice10Dict]
    shipping_price: NotRequired[ShippingPrice10Dict]
