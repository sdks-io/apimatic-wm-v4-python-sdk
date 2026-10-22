from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Meta9(SdkBaseModel):
    """Meta information related to the trends response."""

    currency: Optional[str] = UNSET
    """Currency associated with the price trends of the recommendation.

     Value: USD"""


class Meta9Dict(TypedDict):
    currency: NotRequired[str]
