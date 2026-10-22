from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RichMediaClosedCaption(SdkBaseModel):
    rich_media_caption_language: Optional[str] = Field(default=UNSET, alias="richMediaCaptionLanguage")
    """Human-readable language name for this caption track."""

    rich_media_video_closed_caption_url: Optional[str] = Field(default=UNSET, alias="richMediaVideoClosedCaptionUrl")
    """URL of the closed caption file in ``.vtt`` format."""


class RichMediaClosedCaptionDict(TypedDict):
    rich_media_caption_language: NotRequired[str]
    rich_media_video_closed_caption_url: NotRequired[str]
