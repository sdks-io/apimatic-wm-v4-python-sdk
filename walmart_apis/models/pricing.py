from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .comparison_price import ComparisonPrice, ComparisonPriceDict
from .current_price import CurrentPrice, CurrentPriceDict
from .enums.comparison_price_type import ComparisonPriceTypeOrStr
from .enums.current_price_type import CurrentPriceTypeOrStr
from .enums.price_display_codes1 import PriceDisplayCodes1OrStr
from .enums.process_mode import ProcessModeOrStr


class Pricing(SdkBaseModel):
    effective_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="effectiveDate")
    """This is applicable only for promotions"""

    expiration_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="expirationDate")
    """This is applicable only for promotions"""

    promo_id: Optional[str] = Field(default=UNSET, alias="promoId")
    """This is applicable only for promotions"""

    process_mode: Optional[ProcessModeOrStr] = Field(default=UNSET, alias="processMode")
    """This is applicable only for promotions"""

    current_price_type: CurrentPriceTypeOrStr = Field(alias="currentPriceType")
    current_price: CurrentPrice = Field(alias="currentPrice")
    comparison_price_type: Optional[ComparisonPriceTypeOrStr] = Field(default=UNSET, alias="comparisonPriceType")
    """This is applicable only for promotions"""

    comparison_price: Optional[ComparisonPrice] = Field(default=UNSET, alias="comparisonPrice")
    """This is applicable only for promotions"""

    price_display_codes: Optional[PriceDisplayCodes1OrStr] = Field(default=UNSET, alias="priceDisplayCodes")
    """This is applicable only for promotions"""


class PricingDict(TypedDict):
    effective_date: NotRequired[RFC3339DateTime]
    expiration_date: NotRequired[RFC3339DateTime]
    promo_id: NotRequired[str]
    process_mode: NotRequired[ProcessModeOrStr]
    current_price_type: CurrentPriceTypeOrStr
    current_price: CurrentPriceDict
    comparison_price_type: NotRequired[ComparisonPriceTypeOrStr]
    comparison_price: NotRequired[ComparisonPriceDict]
    price_display_codes: NotRequired[PriceDisplayCodes1OrStr]
