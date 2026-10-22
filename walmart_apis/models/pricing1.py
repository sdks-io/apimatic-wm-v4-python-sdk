from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .comparison_price7 import ComparisonPrice7, ComparisonPrice7Dict
from .current_price7 import CurrentPrice7, CurrentPrice7Dict
from .enums.comparison_price_type6 import ComparisonPriceType6OrStr
from .enums.current_price_type6 import CurrentPriceType6OrStr
from .enums.process_mode6 import ProcessMode6OrStr
from .pickup_discount1 import PickupDiscount1, PickupDiscount1Dict
from .price_display_codes3 import PriceDisplayCodes3, PriceDisplayCodes3Dict


class Pricing1(SdkBaseModel):
    current_price: CurrentPrice7 = Field(alias="currentPrice")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    current_price_type: CurrentPriceType6OrStr = Field(alias="currentPriceType")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    comparison_price: Optional[ComparisonPrice7] = Field(default=UNSET, alias="comparisonPrice")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    comparison_price_type: Optional[ComparisonPriceType6OrStr] = Field(default=UNSET, alias="comparisonPriceType")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    savings_amount: Optional[float] = Field(default=UNSET, alias="savingsAmount")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    savings_percent: Optional[float] = Field(default=UNSET, alias="savingsPercent")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    price_display_codes: Optional[PriceDisplayCodes3] = Field(default=UNSET, alias="priceDisplayCodes")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    pickup_discount: Optional[PickupDiscount1] = Field(default=UNSET, alias="pickupDiscount")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    effective_date: Optional[int] = Field(default=UNSET, alias="effectiveDate")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    expiration_date: Optional[int] = Field(default=UNSET, alias="expirationDate")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    process_mode: Optional[ProcessMode6OrStr] = Field(default=UNSET, alias="processMode")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    pid: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: Global</b>"""


class Pricing1Dict(TypedDict):
    current_price: CurrentPrice7Dict
    current_price_type: CurrentPriceType6OrStr
    comparison_price: NotRequired[ComparisonPrice7Dict]
    comparison_price_type: NotRequired[ComparisonPriceType6OrStr]
    savings_amount: NotRequired[float]
    savings_percent: NotRequired[float]
    price_display_codes: NotRequired[PriceDisplayCodes3Dict]
    pickup_discount: NotRequired[PickupDiscount1Dict]
    effective_date: NotRequired[int]
    expiration_date: NotRequired[int]
    process_mode: NotRequired[ProcessMode6OrStr]
    pid: NotRequired[str]
