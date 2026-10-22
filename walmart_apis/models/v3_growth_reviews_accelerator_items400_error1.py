from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error51 import Error51, Error51Dict


class V3GrowthReviewsAcceleratorItems400Error1(SdkBaseModel):
    status_code: Optional[int] = Field(default=UNSET, alias="statusCode")
    errors: Optional[list[Error51]] = UNSET


class V3GrowthReviewsAcceleratorItems400Error1Dict(TypedDict):
    status_code: NotRequired[int]
    errors: NotRequired[list[Error51Dict]]
