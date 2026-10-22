from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .additional_attributes1 import AdditionalAttributes1, AdditionalAttributes1Dict
from .item_identifier_type import ItemIdentifierType, ItemIdentifierTypeDict
from .money_type import MoneyType, MoneyTypeDict
from .pricing_list_type import PricingListType, PricingListTypeDict
from .rebate import Rebate, RebateDict


class ItemPriceType(SdkBaseModel):
    item_identifier: ItemIdentifierType = Field(alias="itemIdentifier")
    pricing_list: PricingListType = Field(alias="pricingList")
    max_sales_retail_price: Optional[MoneyType] = Field(default=UNSET, alias="maxSalesRetailPrice")
    min_advt_price: Optional[MoneyType] = Field(default=UNSET, alias="minAdvtPrice")
    rebate: Optional[Rebate] = UNSET
    additional_attributes: Optional[AdditionalAttributes1] = Field(default=UNSET, alias="additionalAttributes")


class ItemPriceTypeDict(TypedDict):
    item_identifier: ItemIdentifierTypeDict
    pricing_list: PricingListTypeDict
    max_sales_retail_price: NotRequired[MoneyTypeDict]
    min_advt_price: NotRequired[MoneyTypeDict]
    rebate: NotRequired[RebateDict]
    additional_attributes: NotRequired[AdditionalAttributes1Dict]
