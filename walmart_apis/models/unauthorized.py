from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error11 import Error11, Error11Dict


class Unauthorized(SdkBaseModel):
    error: Optional[list[Error11]] = UNSET


class UnauthorizedDict(TypedDict):
    error: NotRequired[list[Error11Dict]]
