from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .rich_media_closed_caption import RichMediaClosedCaption, RichMediaClosedCaptionDict


class VideoAssetDetailPayload(SdkBaseModel):
    """Rich media content for a VIDEO type asset."""

    media_type: Literal["VIDEO"] = Field(default="VIDEO", alias="mediaType")
    """Discriminator field identifying this as a VIDEO asset."""

    rich_media_closed_caption: Optional[list[RichMediaClosedCaption]] = Field(
        default=UNSET, alias="richMediaClosedCaption"
    )
    """Closed caption tracks associated with the video. May be empty if no captions are available."""

    rich_media_video_asset_url: Optional[str] = Field(default=UNSET, alias="richMediaVideoAssetUrl")
    """URL of the video asset file."""

    rich_media_video_category: Optional[str] = Field(default=UNSET, alias="richMediaVideoCategory")
    """Category classifying the type of video content."""

    rich_media_video_title: Optional[str] = Field(default=UNSET, alias="richMediaVideoTitle")
    """Display title of the video."""

    rich_media_video_thumbnail_url: Optional[str] = Field(default=UNSET, alias="richMediaVideoThumbnailUrl")
    """URL of the video thumbnail image."""


class VideoAssetDetailPayloadDict(TypedDict):
    media_type: Literal["VIDEO"]
    rich_media_closed_caption: NotRequired[list[RichMediaClosedCaptionDict]]
    rich_media_video_asset_url: NotRequired[str]
    rich_media_video_category: NotRequired[str]
    rich_media_video_title: NotRequired[str]
    rich_media_video_thumbnail_url: NotRequired[str]
