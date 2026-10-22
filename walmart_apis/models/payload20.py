from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Payload20(SdkBaseModel):
    """Response payload containing operation results."""

    feed_id: Optional[str] = Field(default=UNSET, alias="feedId")
    """A unique ID returned from the Bulk Upload API, used for tracking the feed file."""

    error_count: Optional[int] = Field(default=UNSET, alias="errorCount")
    """Number of errors encountered during processing."""


class Payload20Dict(TypedDict):
    feed_id: NotRequired[str]
    error_count: NotRequired[int]
