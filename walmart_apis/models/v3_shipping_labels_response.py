from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data4 import Data4, Data4Dict


class V3ShippingLabelsResponse(SdkBaseModel):
    data: Optional[Data4] = UNSET
    """Response payload containing the generated label tracking details and, when requested, the label file."""


class V3ShippingLabelsResponseDict(TypedDict):
    data: NotRequired[Data4Dict]
