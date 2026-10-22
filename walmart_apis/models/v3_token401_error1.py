from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class V3Token401Error1(SdkBaseModel):
    error: str = "invalid_client"
    error_description: str = "Bad client credentials"


class V3Token401Error1Dict(TypedDict):
    error: NotRequired[str]
    error_description: NotRequired[str]
