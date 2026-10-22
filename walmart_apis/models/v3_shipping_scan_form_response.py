from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data9 import Data9, Data9Dict


class V3ShippingScanFormResponse(SdkBaseModel):
    data: Optional[Data9] = UNSET
    """Response payload for the operation."""


class V3ShippingScanFormResponseDict(TypedDict):
    data: NotRequired[Data9Dict]
