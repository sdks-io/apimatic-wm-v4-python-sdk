from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Meta(SdkBaseModel):
    total_count: Optional[float] = Field(default=UNSET, alias="totalCount")
    """Total number of Skus of the Seller. Example: '235'"""

    next_cursor: Optional[str] = Field(default=UNSET, alias="nextCursor")
    """Used for pagination to fetch the next set of items."""


class MetaDict(TypedDict):
    total_count: NotRequired[float]
    next_cursor: NotRequired[str]
