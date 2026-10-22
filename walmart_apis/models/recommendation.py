from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Recommendation(SdkBaseModel):
    product_name: Optional[str] = UNSET
    short_description: Optional[str] = UNSET


class RecommendationDict(TypedDict):
    product_name: NotRequired[str]
    short_description: NotRequired[str]
