from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VariantInfo(SdkBaseModel):
    """Variants information."""

    name: Optional[str] = UNSET
    """Indicates the item attribute name for which variants are available. Example - color, size"""

    value: Optional[str] = UNSET
    """Indicates the value of item attribute for which variants are available. Example - blue, small"""


class VariantInfoDict(TypedDict):
    name: NotRequired[str]
    value: NotRequired[str]
