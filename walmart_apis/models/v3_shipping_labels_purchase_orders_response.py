from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data7 import Data7, Data7Dict


class V3ShippingLabelsPurchaseOrdersResponse(SdkBaseModel):
    data: Optional[list[Data7]] = UNSET
    """List of label details generated for the specified purchase order ID."""


class V3ShippingLabelsPurchaseOrdersResponseDict(TypedDict):
    data: NotRequired[list[Data7Dict]]
