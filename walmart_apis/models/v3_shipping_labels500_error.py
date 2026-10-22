from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error61 import Error61, Error61Dict


class V3ShippingLabels500Error(SdkBaseModel):
    errors: Optional[list[Error61]] = UNSET
    """List of error details describing why the request failed."""


class V3ShippingLabels500ErrorDict(TypedDict):
    errors: NotRequired[list[Error61Dict]]
