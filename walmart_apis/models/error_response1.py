from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error2 import Error2, Error2Dict


class ErrorResponse1(SdkBaseModel):
    errors: Optional[list[Error2]] = UNSET


class ErrorResponse1Dict(TypedDict):
    errors: NotRequired[list[Error2Dict]]
