from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class FeedId(SdkBaseModel):
    feed_id: Optional[str] = Field(default=UNSET, alias="feedId")
    """A unique identifier, which is returned by the Bulk Upload API, used to track and manage the status of the feed
    file."""

    additional_attributes: OptionalNullable[Any] = Field(default=UNSET, alias="additionalAttributes")
    errors: OptionalNullable[Any] = UNSET


class FeedIdDict(TypedDict):
    feed_id: NotRequired[str]
    additional_attributes: NotRequired[Any | None]
    errors: NotRequired[Any | None]
