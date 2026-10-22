from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error1 import Error1, Error1Dict


class V3Token500Error(SdkBaseModel):
    error: Optional[list[Error1]] = UNSET


class V3Token500ErrorDict(TypedDict):
    error: NotRequired[list[Error1Dict]]
