from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Approved(SdkBaseModel):
    """Required only when decision is APPROVED"""

    product_name: Optional[str] = UNSET
    """SEO recommended value for the new product name"""

    short_description: Optional[str] = UNSET
    """SEO recommended value for the new product description"""


class ApprovedDict(TypedDict):
    product_name: NotRequired[str]
    short_description: NotRequired[str]
