from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ShippingSpeed(SdkBaseModel):
    shipping_type: Optional[str] = Field(default=UNSET, alias="shippingType")
    issue_title: Optional[str] = Field(default=UNSET, alias="issueTitle")
    issue_desc: Optional[str] = Field(default=UNSET, alias="issueDesc")
    score: Optional[int] = UNSET


class ShippingSpeedDict(TypedDict):
    shipping_type: NotRequired[str]
    issue_title: NotRequired[str]
    issue_desc: NotRequired[str]
    score: NotRequired[int]
