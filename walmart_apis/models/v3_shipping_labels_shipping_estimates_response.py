from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data6 import Data6, Data6Dict


class V3ShippingLabelsShippingEstimatesResponse(SdkBaseModel):
    data: Optional[Data6] = UNSET
    """Response payload containing the list of shipping cost estimates for available services."""


class V3ShippingLabelsShippingEstimatesResponseDict(TypedDict):
    data: NotRequired[Data6Dict]
