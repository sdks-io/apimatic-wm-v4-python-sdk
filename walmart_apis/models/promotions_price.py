from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money_type import MoneyType, MoneyTypeDict


class PromotionsPrice(SdkBaseModel):
    value: Optional[MoneyType] = UNSET
    uom_type: Optional[str] = Field(default=UNSET, alias="uomType")
    min_value: Optional[MoneyType] = Field(default=UNSET, alias="minValue")
    max_value: Optional[MoneyType] = Field(default=UNSET, alias="maxValue")
    per_unit_value: Optional[MoneyType] = Field(default=UNSET, alias="perUnitValue")
    min_unit_value: Optional[MoneyType] = Field(default=UNSET, alias="minUnitValue")
    max_unit_value: Optional[MoneyType] = Field(default=UNSET, alias="maxUnitValue")


class PromotionsPriceDict(TypedDict):
    value: NotRequired[MoneyTypeDict]
    uom_type: NotRequired[str]
    min_value: NotRequired[MoneyTypeDict]
    max_value: NotRequired[MoneyTypeDict]
    per_unit_value: NotRequired[MoneyTypeDict]
    min_unit_value: NotRequired[MoneyTypeDict]
    max_unit_value: NotRequired[MoneyTypeDict]
