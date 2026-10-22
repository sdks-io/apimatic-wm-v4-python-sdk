from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error11 import Error11, Error11Dict


class V3GrowthReviewsAcceleratorItemsStatus401Error1(SdkBaseModel):
    error: Optional[list[Error11]] = UNSET


class V3GrowthReviewsAcceleratorItemsStatus401Error1Dict(TypedDict):
    error: NotRequired[list[Error11Dict]]
