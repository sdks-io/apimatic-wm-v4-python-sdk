from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Header(SdkBaseModel):
    """Response header information."""

    header_attributes: Optional[Any] = Field(default=UNSET, alias="headerAttributes")


class HeaderDict(TypedDict):
    header_attributes: NotRequired[Any]
