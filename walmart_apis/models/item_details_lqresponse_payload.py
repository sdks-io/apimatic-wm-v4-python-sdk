from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_details_for_listing_quality_payload import (
    ItemDetailsForListingQualityPayload,
    ItemDetailsForListingQualityPayloadDict,
)


class ItemDetailsLqresponsePayload(SdkBaseModel):
    next_cursor: Optional[str] = Field(default=UNSET, alias="nextCursor")
    total_items: Optional[str] = Field(default=UNSET, alias="totalItems")
    payload: Optional[list[ItemDetailsForListingQualityPayload]] = UNSET
    status: Optional[str] = UNSET


class ItemDetailsLqresponsePayloadDict(TypedDict):
    next_cursor: NotRequired[str]
    total_items: NotRequired[str]
    payload: NotRequired[list[ItemDetailsForListingQualityPayloadDict]]
    status: NotRequired[str]
