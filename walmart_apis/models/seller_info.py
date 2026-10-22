from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SellerInfo(SdkBaseModel):
    store_front_url: Optional[str] = Field(default=UNSET, alias="storeFrontUrl")
    seller_status: Optional[str] = Field(default=UNSET, alias="sellerStatus")
    payment_status: Optional[str] = Field(default=UNSET, alias="paymentStatus")
    tenure: Optional[int] = UNSET


class SellerInfoDict(TypedDict):
    store_front_url: NotRequired[str]
    seller_status: NotRequired[str]
    payment_status: NotRequired[str]
    tenure: NotRequired[int]
