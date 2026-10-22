from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error51 import Error51, Error51Dict


class V3GrowthReviewsAcceleratorCategories400Error(SdkBaseModel):
    status_code: Optional[int] = Field(default=UNSET, alias="statusCode")
    error: Optional[list[Error51]] = UNSET


class V3GrowthReviewsAcceleratorCategories400ErrorDict(TypedDict):
    status_code: NotRequired[int]
    error: NotRequired[list[Error51Dict]]
