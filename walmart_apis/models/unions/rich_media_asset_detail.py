from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..images360_asset_detail_payload import Images360AssetDetailPayload, Images360AssetDetailPayloadDict
from ..video_asset_detail_payload import VideoAssetDetailPayload, VideoAssetDetailPayloadDict

RichMediaAssetDetail: TypeAlias = Annotated[
    Annotated[VideoAssetDetailPayload, Tag("VIDEO")] | Annotated[Images360AssetDetailPayload, Tag("IMAGES360")],
    WireDiscriminator("mediaType"),
]
"""Asset content details. Structure varies by ``mediaType``: ``VIDEO`` assets contain video URL, optional closed
captions, category, and thumbnail; ``IMAGES360`` assets contain an ordered array of image frame URLs."""

RichMediaAssetDetailDict: TypeAlias = VideoAssetDetailPayloadDict | Images360AssetDetailPayloadDict
