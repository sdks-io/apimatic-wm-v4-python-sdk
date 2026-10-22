from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.comparison_price_type2 import ComparisonPriceType2OrStr
from .enums.current_price_type2 import CurrentPriceType2OrStr
from .enums.process_mode2 import ProcessMode2OrStr
from .pickup_discount import PickupDiscount, PickupDiscountDict
from .price_display_codes import PriceDisplayCodes, PriceDisplayCodesDict
from .promotions_price import PromotionsPrice, PromotionsPriceDict


class PricingType(SdkBaseModel):
    current_price: PromotionsPrice = Field(alias="currentPrice")
    current_price_type: CurrentPriceType2OrStr = Field(alias="currentPriceType")
    comparison_price: Optional[PromotionsPrice] = Field(default=UNSET, alias="comparisonPrice")
    comparison_price_type: Optional[ComparisonPriceType2OrStr] = Field(default=UNSET, alias="comparisonPriceType")
    savings_amount: Optional[float] = Field(default=UNSET, alias="savingsAmount")
    savings_percent: Optional[float] = Field(default=UNSET, alias="savingsPercent")
    price_display_codes: Optional[PriceDisplayCodes] = Field(default=UNSET, alias="priceDisplayCodes")
    pickup_discount: Optional[PickupDiscount] = Field(default=UNSET, alias="pickupDiscount")
    effective_date: Optional[int] = Field(default=UNSET, alias="effectiveDate")
    expiration_date: Optional[int] = Field(default=UNSET, alias="expirationDate")
    process_mode: Optional[ProcessMode2OrStr] = Field(default=UNSET, alias="processMode")
    pid: Optional[str] = UNSET


class PricingTypeDict(TypedDict):
    current_price: PromotionsPriceDict
    current_price_type: CurrentPriceType2OrStr
    comparison_price: NotRequired[PromotionsPriceDict]
    comparison_price_type: NotRequired[ComparisonPriceType2OrStr]
    savings_amount: NotRequired[float]
    savings_percent: NotRequired[float]
    price_display_codes: NotRequired[PriceDisplayCodesDict]
    pickup_discount: NotRequired[PickupDiscountDict]
    effective_date: NotRequired[int]
    expiration_date: NotRequired[int]
    process_mode: NotRequired[ProcessMode2OrStr]
    pid: NotRequired[str]
