from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .status_quantity import StatusQuantity, StatusQuantityDict


class OrderLineStatus(SdkBaseModel):
    status: Optional[str] = UNSET
    """The status of the order line"""

    status_quantity: Optional[StatusQuantity] = Field(default=UNSET, alias="statusQuantity")


class OrderLineStatusDict(TypedDict):
    status: NotRequired[str]
    status_quantity: NotRequired[StatusQuantityDict]
