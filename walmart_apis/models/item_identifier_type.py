from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ItemIdentifierType(SdkBaseModel):
    sku: Optional[str] = UNSET
    offer_id: Optional[str] = Field(default=UNSET, alias="offerId")
    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    wpid: Optional[str] = UNSET
    product_type: Optional[str] = Field(default=UNSET, alias="productType")


class ItemIdentifierTypeDict(TypedDict):
    sku: NotRequired[str]
    offer_id: NotRequired[str]
    item_id: NotRequired[str]
    wpid: NotRequired[str]
    product_type: NotRequired[str]
