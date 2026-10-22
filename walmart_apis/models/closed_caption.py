from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ClosedCaption(SdkBaseModel):
    """A single closed caption entry for a video asset."""

    rich_media_closed_captioning_url: Optional[str] = Field(default=UNSET, alias="richMediaClosedCaptioningUrl")
    """URL of the closed caption file in ``.vtt`` format."""

    rich_media_caption_language: Optional[str] = Field(default=UNSET, alias="richMediaCaptionLanguage")
    """Language of the captions."""


class ClosedCaptionDict(TypedDict):
    rich_media_closed_captioning_url: NotRequired[str]
    rich_media_caption_language: NotRequired[str]
