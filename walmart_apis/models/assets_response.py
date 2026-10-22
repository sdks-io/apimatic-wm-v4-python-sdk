from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .rich_media_asset_payload import RichMediaAssetPayload, RichMediaAssetPayloadDict


class AssetsResponse(SdkBaseModel):
    """Response contains assets details for rich media asset search results."""

    status: Optional[str] = UNSET
    """response status"""

    payload: Optional[list[RichMediaAssetPayload]] = UNSET
    """Array of rich media asset records matching the query."""

    total_records: Optional[int] = Field(default=UNSET, alias="totalRecords")
    """Number of rich media assets returned in the current response."""

    header_attributes: Optional[Any] = Field(default=UNSET, alias="headerAttributes")
    """Additional response header metadata. Typically an empty object."""

    errors: Optional[list[Any]] = UNSET
    """Array of error details. Empty array when no errors occurred."""


class AssetsResponseDict(TypedDict):
    status: NotRequired[str]
    payload: NotRequired[list[RichMediaAssetPayloadDict]]
    total_records: NotRequired[int]
    header_attributes: NotRequired[Any]
    errors: NotRequired[list[Any]]
