from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error11 import Error11, Error11Dict


class V3GrowthReviewsAcceleratorItemsStatus403Error(SdkBaseModel):
    error: Optional[list[Error11]] = UNSET


class V3GrowthReviewsAcceleratorItemsStatus403ErrorDict(TypedDict):
    error: NotRequired[list[Error11Dict]]
