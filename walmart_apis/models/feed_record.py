from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FeedRecord(SdkBaseModel):
    """Information about the individual feed."""

    feed_id: Optional[str] = Field(default=UNSET, alias="feedId")
    """A unique ID used for tracking the Feed File."""

    feed_source: Optional[str] = Field(default=UNSET, alias="feedSource")
    """The source of the feed."""

    feed_type: Optional[str] = Field(default=UNSET, alias="feedType")
    """Indicates the feed type."""

    partner_id: Optional[str] = Field(default=UNSET, alias="partnerId")
    """Indicates the seller ID."""

    items_received: Optional[int] = Field(default=UNSET, alias="itemsReceived")
    """The number of items received."""

    items_succeeded: Optional[int] = Field(default=UNSET, alias="itemsSucceeded")
    """A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during
    onboarding."""

    items_failed: Optional[int] = Field(default=UNSET, alias="itemsFailed")
    """The number of items in the feed that failed due to a data or system error."""

    items_processing: Optional[int] = Field(default=UNSET, alias="itemsProcessing")
    """The number of items in the feed that are still in progress."""

    feed_status: Optional[str] = Field(default=UNSET, alias="feedStatus")
    """Can be one of the following: RECEIVED, INPROGRESS, PROCESSED, or ERROR. For details, see the definitions listed
    under 'Feed Statuses' at the beginning of this section."""

    feed_date: Optional[int] = Field(default=UNSET, alias="feedDate")
    """The date and time the feed was submitted. Format: yyyymmddThh:mm:ss.xxxz"""

    batch_id: Optional[str] = Field(default=UNSET, alias="batchId")
    """The batch ID for the feed, if provided."""

    modified_dtm: Optional[int] = Field(default=UNSET, alias="modifiedDtm")
    """The most recent time the feed was modified. Format: yyyymmddThh:mm:ss.xxxz"""


class FeedRecordDict(TypedDict):
    feed_id: NotRequired[str]
    feed_source: NotRequired[str]
    feed_type: NotRequired[str]
    partner_id: NotRequired[str]
    items_received: NotRequired[int]
    items_succeeded: NotRequired[int]
    items_failed: NotRequired[int]
    items_processing: NotRequired[int]
    feed_status: NotRequired[str]
    feed_date: NotRequired[int]
    batch_id: NotRequired[str]
    modified_dtm: NotRequired[int]
