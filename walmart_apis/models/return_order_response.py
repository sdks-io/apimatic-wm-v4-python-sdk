from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta1 import Meta1, Meta1Dict
from .return_order import ReturnOrder, ReturnOrderDict


class ReturnOrderResponse(SdkBaseModel):
    meta: Optional[Meta1] = UNSET
    return_orders: Optional[list[ReturnOrder]] = Field(default=UNSET, alias="returnOrders")
    """List of returns for the seller.<br><b style='color:green;'>Market availability: Global</b>"""


class ReturnOrderResponseDict(TypedDict):
    meta: NotRequired[Meta1Dict]
    return_orders: NotRequired[list[ReturnOrderDict]]
