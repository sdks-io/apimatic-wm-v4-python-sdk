from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error6 import Error6, Error6Dict


class ErrorResponse2(SdkBaseModel):
    status: Optional[str] = UNSET
    errors: Optional[list[Error6]] = UNSET


class ErrorResponse2Dict(TypedDict):
    status: NotRequired[str]
    errors: NotRequired[list[Error6Dict]]
