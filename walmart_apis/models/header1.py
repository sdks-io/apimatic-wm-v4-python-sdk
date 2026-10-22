from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Header1(SdkBaseModel):
    """Response header information."""

    header_attributes: Optional[Any] = Field(default=UNSET, alias="headerAttributes")


class Header1Dict(TypedDict):
    header_attributes: NotRequired[Any]
