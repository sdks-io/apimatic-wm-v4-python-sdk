from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V3InsightsProsellerbadge400Error(SdkBaseModel):
    error_code: Optional[str] = Field(default=UNSET, alias="errorCode")
    error_description: Optional[str] = Field(default=UNSET, alias="errorDescription")


class V3InsightsProsellerbadge400ErrorDict(TypedDict):
    error_code: NotRequired[str]
    error_description: NotRequired[str]
