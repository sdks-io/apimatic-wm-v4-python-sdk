from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class V3Token400Error(SdkBaseModel):
    error: Optional[list[Error]] = UNSET


class V3Token400ErrorDict(TypedDict):
    error: NotRequired[list[ErrorDict]]
