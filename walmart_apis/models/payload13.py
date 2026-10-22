from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .item_identifiers import ItemIdentifiers, ItemIdentifiersDict


class Payload13(SdkBaseModel):
    item_identifier: Optional[ItemIdentifiers] = Field(default=UNSET, alias="itemIdentifier")
    max_sales_retail_price: OptionalNullable[str] = Field(default=UNSET, alias="maxSalesRetailPrice")
    min_advt_price: OptionalNullable[str] = Field(default=UNSET, alias="minAdvtPrice")
    rebate: OptionalNullable[str] = UNSET


class Payload13Dict(TypedDict):
    item_identifier: NotRequired[ItemIdentifiersDict]
    max_sales_retail_price: NotRequired[str | None]
    min_advt_price: NotRequired[str | None]
    rebate: NotRequired[str | None]
