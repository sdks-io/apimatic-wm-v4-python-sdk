from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1SettingsGettaxformprofile400Error1(SdkBaseModel):
    error_code: str = Field(alias="errorCode")
    """The error code identifying the type of error."""

    message: str
    """A descriptive message explaining the error."""

    status: int
    """The HTTP status code."""


class V1SettingsGettaxformprofile400Error1Dict(TypedDict):
    error_code: str
    message: str
    status: int
