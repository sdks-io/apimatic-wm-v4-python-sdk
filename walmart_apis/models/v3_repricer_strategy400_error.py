from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V3RepricerStrategy400Error(SdkBaseModel):
    status: Optional[str] = UNSET
    error_message: Optional[str] = Field(default=UNSET, alias="errorMessage")


class V3RepricerStrategy400ErrorDict(TypedDict):
    status: NotRequired[str]
    error_message: NotRequired[str]
