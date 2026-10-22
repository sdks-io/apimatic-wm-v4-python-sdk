from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.feed_status import FeedStatusOrStr
from .error3 import Error3, Error3Dict
from .ingestion_errors import IngestionErrors, IngestionErrorsDict
from .item_details5 import ItemDetails5, ItemDetails5Dict


class PartnerFeedResponse(SdkBaseModel):
    errors: Optional[list[Error3]] = UNSET
    feed_id: Optional[str] = Field(default=UNSET, alias="feedId")
    """A unique ID used for tracking the Feed File."""

    feed_status: Optional[FeedStatusOrStr] = Field(default=UNSET, alias="feedStatus")
    """Can be one of the following: RECEIVED, INPROGRESS, PROCESSED, or ERROR"""

    ingestion_errors: Optional[IngestionErrors] = Field(default=UNSET, alias="ingestionErrors")
    """List of errors for an item."""

    items_received: Optional[int] = Field(default=UNSET, alias="itemsReceived")
    """The number of items received. in the feed."""

    items_succeeded: Optional[int] = Field(default=UNSET, alias="itemsSucceeded")
    """The number of items in the feed that processed successfully."""

    items_failed: Optional[int] = Field(default=UNSET, alias="itemsFailed")
    """The number of items in the feed that failed due to a data or system error."""

    items_processing: Optional[int] = Field(default=UNSET, alias="itemsProcessing")
    """The number of items in the feed that are still processing."""

    offset: Optional[int] = UNSET
    """The object response to the starting number, where 0 is the first entity available for request."""

    limit: Optional[int] = UNSET
    """The number of items returned. Cannot be greater than 1000."""

    item_details: Optional[ItemDetails5] = Field(default=UNSET, alias="itemDetails")
    """List of ingestion status details for items in the feed."""


class PartnerFeedResponseDict(TypedDict):
    errors: NotRequired[list[Error3Dict]]
    feed_id: NotRequired[str]
    feed_status: NotRequired[FeedStatusOrStr]
    ingestion_errors: NotRequired[IngestionErrorsDict]
    items_received: NotRequired[int]
    items_succeeded: NotRequired[int]
    items_failed: NotRequired[int]
    items_processing: NotRequired[int]
    offset: NotRequired[int]
    limit: NotRequired[int]
    item_details: NotRequired[ItemDetails5Dict]
