from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .video_asset import VideoAsset, VideoAssetDict


class VisibleVideoPayload(SdkBaseModel):
    """Visible block for a video rich media asset. Discriminator for this block is set as subcategory: ``VIDEO``"""

    video: Optional[VideoAsset] = Field(default=UNSET, alias="Video")
    """Video rich media block. Required when ``SupplierItemFeedHeader.subCategory`` is ``video``."""


class VisibleVideoPayloadDict(TypedDict):
    video: NotRequired[VideoAssetDict]
