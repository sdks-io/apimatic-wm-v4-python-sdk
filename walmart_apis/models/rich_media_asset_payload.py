from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .associated_item_payload import AssociatedItemPayload, AssociatedItemPayloadDict
from .enums.media_type import MediaTypeOrStr
from .enums.source import SourceOrStr
from .unions.rich_media_asset_detail import RichMediaAssetDetail, RichMediaAssetDetailDict


class RichMediaAssetPayload(SdkBaseModel):
    hash: Optional[str] = UNSET
    """SHA-1 hash that uniquely identifies this rich media asset."""

    media_title: Optional[str] = Field(default=UNSET, alias="mediaTitle")
    """Display title for the rich media asset."""

    media_type: Optional[MediaTypeOrStr] = Field(default=UNSET, alias="mediaType")
    """Type of rich media asset. Determines the structure of the ``richMediaAsset`` object."""

    source: Optional[SourceOrStr] = UNSET
    """Originating source of the rich media asset. Possible values: ``MARKETPLACE_PARTNER``, ``SELLER_API``"""

    items: Optional[list[AssociatedItemPayload]] = UNSET
    """List of items associated with this rich media asset."""

    rich_media_asset: Optional[RichMediaAssetDetail] = Field(default=UNSET, alias="richMediaAsset")
    """Asset content details. Structure varies by ``mediaType``: ``VIDEO`` assets contain video URL, optional closed
    captions, category, and thumbnail; ``IMAGES360`` assets contain an ordered array of image frame URLs."""

    added_dtm: Optional[str] = Field(default=UNSET, alias="addedDtm")
    """Timestamp when the asset was first created, in epoch milliseconds."""

    updated_dtm: Optional[str] = Field(default=UNSET, alias="updatedDtm")
    """Timestamp when the asset record was last updated, in epoch milliseconds."""


class RichMediaAssetPayloadDict(TypedDict):
    hash: NotRequired[str]
    media_title: NotRequired[str]
    media_type: NotRequired[MediaTypeOrStr]
    source: NotRequired[SourceOrStr]
    items: NotRequired[list[AssociatedItemPayloadDict]]
    rich_media_asset: NotRequired[RichMediaAssetDetailDict]
    added_dtm: NotRequired[str]
    updated_dtm: NotRequired[str]
