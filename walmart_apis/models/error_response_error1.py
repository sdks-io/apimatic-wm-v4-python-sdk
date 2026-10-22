from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error2 import Error2, Error2Dict


class ErrorResponseError1(SdkBaseModel):
    errors: Optional[list[Error2]] = UNSET


class ErrorResponseError1Dict(TypedDict):
    errors: NotRequired[list[Error2Dict]]
