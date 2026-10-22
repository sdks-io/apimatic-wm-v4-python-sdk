from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error11 import Error11, Error11Dict


class V3GrowthReviewsAcceleratorItemsStatus500Error1(SdkBaseModel):
    status_code: Optional[int] = Field(default=UNSET, alias="statusCode")
    errors: Optional[list[Error11]] = UNSET


class V3GrowthReviewsAcceleratorItemsStatus500Error1Dict(TypedDict):
    status_code: NotRequired[int]
    errors: NotRequired[list[Error11Dict]]
