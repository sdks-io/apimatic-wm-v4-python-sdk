from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Headers(SdkBaseModel):
    total_count: Optional[int] = Field(default=UNSET, alias="totalCount")
    """Total number of results for query."""

    limit: Optional[int] = UNSET
    """Information about the quantity in inventory."""

    offset: Optional[int] = UNSET
    """Offset is the number of records you wish to skip before selecting results."""


class HeadersDict(TypedDict):
    total_count: NotRequired[int]
    limit: NotRequired[int]
    offset: NotRequired[int]
