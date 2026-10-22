from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fast_shipping_speed5 import FastShippingSpeed5, FastShippingSpeed5Dict
from .free_shipping_speed5 import FreeShippingSpeed5, FreeShippingSpeed5Dict
from .price3 import Price3, Price3Dict
from .publish_and_transactable3 import PublishAndTransactable3, PublishAndTransactable3Dict
from .shipping_speed4 import ShippingSpeed4, ShippingSpeed4Dict


class Offer2(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    issue_count: Optional[int] = Field(default=UNSET, alias="issueCount")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    price: Optional[Price3] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    shipping_speed: Optional[ShippingSpeed4] = Field(default=UNSET, alias="shippingSpeed")
    """<br><b style='color:green;'>Market availability: US only</b>"""

    publish_and_transactable: Optional[PublishAndTransactable3] = Field(default=UNSET, alias="publishAndTransactable")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    fast_shipping_speed: Optional[FastShippingSpeed5] = Field(default=UNSET, alias="fastShippingSpeed")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    free_shipping_speed: Optional[FreeShippingSpeed5] = Field(default=UNSET, alias="freeShippingSpeed")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class Offer2Dict(TypedDict):
    issue_count: NotRequired[int]
    price: NotRequired[Price3Dict]
    shipping_speed: NotRequired[ShippingSpeed4Dict]
    publish_and_transactable: NotRequired[PublishAndTransactable3Dict]
    fast_shipping_speed: NotRequired[FastShippingSpeed5Dict]
    free_shipping_speed: NotRequired[FreeShippingSpeed5Dict]
