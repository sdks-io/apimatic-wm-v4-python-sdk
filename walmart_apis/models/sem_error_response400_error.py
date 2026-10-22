from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sem_error400 import SemError400, SemError400Dict


class SemErrorResponse400Error(SdkBaseModel):
    error: Optional[list[SemError400]] = UNSET
    """An array containing error messages related to the request."""


class SemErrorResponse400ErrorDict(TypedDict):
    error: NotRequired[list[SemError400Dict]]
