from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .order_line_statuses import OrderLineStatuses, OrderLineStatusesDict


class OrderLine(SdkBaseModel):
    line_number: str = Field(alias="lineNumber")
    """The order line number"""

    order_line_statuses: OrderLineStatuses = Field(alias="orderLineStatuses")


class OrderLineDict(TypedDict):
    line_number: str
    order_line_statuses: OrderLineStatusesDict
