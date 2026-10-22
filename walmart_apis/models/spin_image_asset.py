from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.media_operations import MediaOperationsOrStr


class SpinImageAsset(SdkBaseModel):
    """360-spin image rich media block. Required when ``SupplierItemFeedHeader.subCategory`` is ``360_spin_image``."""

    rich_media_image_url: list[str] = Field(alias="richMediaImageUrl")
    """Ordered list of 24 accessible 360-spin image frame URLs, numbered sequentially with suffix from ``_1`` to
    ``_24``."""

    rich_media360_spin_title: Optional[str] = Field(default=UNSET, alias="richMedia360SpinTitle")
    """Display title for the 360-spin image."""

    media_operations: OptionalNullable[MediaOperationsOrStr] = Field(default=UNSET, alias="mediaOperations")
    """Operation type. Allowed values: ``Delink`` and ``null``(empty). Set to ``Delink`` to remove the GTIN association
    from this asset. Set to ``null`` (empty) for create/edit operations."""


class SpinImageAssetDict(TypedDict):
    rich_media_image_url: list[str]
    rich_media360_spin_title: NotRequired[str]
    media_operations: NotRequired[MediaOperationsOrStr | None]
