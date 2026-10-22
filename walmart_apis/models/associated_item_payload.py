from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.media_type1 import MediaType1OrStr


class AssociatedItemPayload(SdkBaseModel):
    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    """Walmart-generated item identifier."""

    gtin: Optional[str] = UNSET
    """Global Trade Item Number (GTIN-14) for the linked item."""

    updated_dtm: Optional[str] = Field(default=UNSET, alias="updatedDtm")
    """Timestamp of the most recent item-asset linkage update, in epoch milliseconds."""

    media_type: Optional[MediaType1OrStr] = Field(default=UNSET, alias="mediaType")
    """Media type as recorded for this specific item linkage."""

    locale: Optional[str] = UNSET
    """Locale for the item-asset association (BCP 47 format with underscore separator)."""

    status: Optional[str] = UNSET
    """Publication status of this asset for the linked item."""


class AssociatedItemPayloadDict(TypedDict):
    item_id: NotRequired[str]
    gtin: NotRequired[str]
    updated_dtm: NotRequired[str]
    media_type: NotRequired[MediaType1OrStr]
    locale: NotRequired[str]
    status: NotRequired[str]
