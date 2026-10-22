from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.field_model import FieldModel, FieldModelOrStr
from .enums.order import Order, OrderOrStr


class WsrSort(SdkBaseModel):
    """Sort configuration for ordering the report results.

    **Defaults**: field="gmv", order="DESC"
    """

    field: FieldModelOrStr = FieldModel.GMV
    """Attribute on which sorting needs to be performed.

    **Supported Values**: clicks, gmv, orders **Default**: gmv"""

    order: OrderOrStr = Order.DESC
    """Sorting order.

    **Default**: DESC"""


class WsrSortDict(TypedDict):
    field: NotRequired[FieldModelOrStr]
    order: NotRequired[OrderOrStr]
