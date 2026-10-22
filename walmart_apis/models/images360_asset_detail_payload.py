from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Images360AssetDetailPayload(SdkBaseModel):
    """Rich media content for an ``IMAGES360`` type asset."""

    media_type: Literal["IMAGES360"] = Field(default="IMAGES360", alias="mediaType")
    """Discriminator field identifying this as an IMAGES360 asset."""

    rich_media_image_url: Optional[list[str]] = Field(default=UNSET, alias="richMediaImageUrl")
    """Ordered list of 360-spin image frame URLs, numbered sequentially from ``_1`` to ``_24``."""


class Images360AssetDetailPayloadDict(TypedDict):
    media_type: Literal["IMAGES360"]
    rich_media_image_url: NotRequired[list[str]]
