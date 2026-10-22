from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .closed_caption import ClosedCaption, ClosedCaptionDict
from .enums.media_operations import MediaOperationsOrStr


class VideoAsset(SdkBaseModel):
    """Video rich media block. Required when ``SupplierItemFeedHeader.subCategory`` is ``video``."""

    rich_media_video_asset_url: str = Field(alias="richMediaVideoAssetUrl")
    """Accessible URL for the hosted video asset."""

    rich_media_video_title: str = Field(alias="richMediaVideoTitle")
    """Display title for the video."""

    rich_media_video_thumbnail_url: Optional[str] = Field(default=UNSET, alias="richMediaVideoThumbnailUrl")
    """Accessible URL for the video thumbnail image."""

    rich_media_video_category: Literal["Product Overview"] = Field(
        default="Product Overview", alias="richMediaVideoCategory"
    )
    """Video category label. Allowed value: ``Product Overview``."""

    media_operations: OptionalNullable[MediaOperationsOrStr] = Field(default=UNSET, alias="mediaOperations")
    """Operation type. Allowed values: ``Delink`` and ``null``(empty). Set to ``Delink`` to remove the GTIN association
    from this asset. Set to ``null`` (empty) for create/edit operations."""

    rich_media_closed_caption: Optional[list[ClosedCaption]] = Field(default=UNSET, alias="richMediaClosedCaption")
    """Closed caption entry for the video. Maximum allowed: 1."""


class VideoAssetDict(TypedDict):
    rich_media_video_asset_url: str
    rich_media_video_title: str
    rich_media_video_thumbnail_url: NotRequired[str]
    rich_media_video_category: Literal["Product Overview"]
    media_operations: NotRequired[MediaOperationsOrStr | None]
    rich_media_closed_caption: NotRequired[list[ClosedCaptionDict]]
