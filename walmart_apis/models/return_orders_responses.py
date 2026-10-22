from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta12 import Meta12, Meta12Dict
from .return_order1 import ReturnOrder1, ReturnOrder1Dict


class ReturnOrdersResponses(SdkBaseModel):
    meta: Optional[Meta12] = UNSET
    """Meta data about the list.<br><b style='color:green;'>Market availability: MX</b>"""

    return_orders: Optional[list[ReturnOrder1]] = Field(default=UNSET, alias="returnOrders")
    """returnOrders.<br><b style='color:green;'>Market availability: MX</b>"""


class ReturnOrdersResponsesDict(TypedDict):
    meta: NotRequired[Meta12Dict]
    return_orders: NotRequired[list[ReturnOrder1Dict]]
