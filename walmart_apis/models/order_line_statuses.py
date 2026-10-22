from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .order_line_status import OrderLineStatus, OrderLineStatusDict


class OrderLineStatuses(SdkBaseModel):
    order_line_status: Optional[list[OrderLineStatus]] = Field(default=UNSET, alias="orderLineStatus")


class OrderLineStatusesDict(TypedDict):
    order_line_status: NotRequired[list[OrderLineStatusDict]]
