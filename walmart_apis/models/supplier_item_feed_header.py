from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.sub_category import SubCategoryOrStr


class SupplierItemFeedHeader(SdkBaseModel):
    """Metadata header for the rich media feed."""

    feed_type: Literal["OMNI_RICH_MEDIA"] = Field(default="OMNI_RICH_MEDIA", alias="feedType")
    """Feed type identifier. Allowed value: ``OMNI_RICH_MEDIA``."""

    locale: str
    """Locale code for the feed content."""

    version: str
    """Schema version string for the feed."""

    sub_category: SubCategoryOrStr = Field(alias="subCategory")
    """Rich media sub-category that determines the required Visible block. Allowed values: ``video``,
    ``360_spin_image``."""

    subset: Literal["EXTERNAL"] = "EXTERNAL"
    """Subset that identifies the feed source or audience. Allowed value: ``EXTERNAL``."""


class SupplierItemFeedHeaderDict(TypedDict):
    feed_type: Literal["OMNI_RICH_MEDIA"]
    locale: str
    version: str
    sub_category: SubCategoryOrStr
    subset: Literal["EXTERNAL"]
