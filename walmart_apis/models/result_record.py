from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .feed_record import FeedRecord, FeedRecordDict


class ResultRecord(SdkBaseModel):
    """Specifies the feed status results."""

    feed: Optional[list[FeedRecord]] = UNSET
    """Specifies the feed status results."""


class ResultRecordDict(TypedDict):
    feed: NotRequired[list[FeedRecordDict]]
