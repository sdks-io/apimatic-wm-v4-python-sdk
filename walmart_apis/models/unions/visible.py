from __future__ import annotations

from typing import TypeAlias

from ..visible360_image_payload import Visible360ImagePayload, Visible360ImagePayloadDict
from ..visible_video_payload import VisibleVideoPayload, VisibleVideoPayloadDict

Visible: TypeAlias = VisibleVideoPayload | Visible360ImagePayload
"""The visible block for rich media. The expected structure depends on ``SupplierItemFeedHeader.subCategory``.
Discriminator is based on ``SupplierItemFeedHeader.subCategory``"""

VisibleDict: TypeAlias = VisibleVideoPayloadDict | Visible360ImagePayloadDict
