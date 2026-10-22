from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .spin_image_asset import SpinImageAsset, SpinImageAssetDict


class Visible360ImagePayload(SdkBaseModel):
    """Visible block for a 360-spin image rich media asset. Discriminator for this block is set as subcategory:
    ``IMAGES360``"""

    spin_image360: Optional[SpinImageAsset] = Field(default=UNSET, alias="360SpinImage")
    """360-spin image rich media block. Required when ``SupplierItemFeedHeader.subCategory`` is ``360_spin_image``."""


class Visible360ImagePayloadDict(TypedDict):
    spin_image360: NotRequired[SpinImageAssetDict]
