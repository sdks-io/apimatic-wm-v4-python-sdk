from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.content import ContentOrStr
from .enums.feeds import FeedsOrStr
from .enums.inventory import InventoryOrStr
from .enums.item import ItemOrStr
from .enums.lagtime import LagtimeOrStr
from .enums.orders import OrdersOrStr
from .enums.price import PriceOrStr
from .enums.reports import ReportsOrStr
from .enums.returns import ReturnsOrStr
from .enums.rules import RulesOrStr
from .enums.shipping import ShippingOrStr


class Scopes(SdkBaseModel):
    """The API categories with their corresponding access levels"""

    reports: Optional[ReportsOrStr] = UNSET
    item: Optional[ItemOrStr] = UNSET
    shipping: Optional[ShippingOrStr] = UNSET
    price: Optional[PriceOrStr] = UNSET
    lagtime: Optional[LagtimeOrStr] = UNSET
    feeds: Optional[FeedsOrStr] = UNSET
    returns: Optional[ReturnsOrStr] = UNSET
    orders: Optional[OrdersOrStr] = UNSET
    rules: Optional[RulesOrStr] = UNSET
    inventory: Optional[InventoryOrStr] = UNSET
    content: Optional[ContentOrStr] = UNSET


class ScopesDict(TypedDict):
    reports: NotRequired[ReportsOrStr]
    item: NotRequired[ItemOrStr]
    shipping: NotRequired[ShippingOrStr]
    price: NotRequired[PriceOrStr]
    lagtime: NotRequired[LagtimeOrStr]
    feeds: NotRequired[FeedsOrStr]
    returns: NotRequired[ReturnsOrStr]
    orders: NotRequired[OrdersOrStr]
    rules: NotRequired[RulesOrStr]
    inventory: NotRequired[InventoryOrStr]
    content: NotRequired[ContentOrStr]
