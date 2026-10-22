from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.promotion_placement import PromotionPlacementOrStr
from .enums.promotion_setting_action1 import PromotionSettingAction1OrStr
from .enums.promotion_type1 import PromotionType1OrStr


class PromotionInformation1(SdkBaseModel):
    promotion_setting_action: Optional[PromotionSettingAction1OrStr] = Field(
        default=UNSET, alias="promotionSettingAction"
    )
    """| Market | Translation |
    | --- | ----------- |
    | US | ["Create", "Delete","Replace All"]|
    <br><b style='color:green;'>Market availability: US"""

    promotion_placement: Optional[PromotionPlacementOrStr] = Field(default=UNSET, alias="promotionPlacement")
    """Controls where discounted price is revealed to customers.<br><b style='color:green;'>Market availability: US"""

    promotion_type: Optional[PromotionType1OrStr] = Field(default=UNSET, alias="promotionType")
    """| Market | Translation |
    | --- | ----------- |
    | US | ["Clearance", "Reduced"]|

    <br><b style='color:green;'>Market availability: US</b>"""

    promotion_price: Optional[float] = Field(default=UNSET, alias="promotionPrice")
    """Promotion price that you want to set for the SKU..<br> promotionPrice is required for Create.<br><b
    style='color:green;'>Market availability: US"""

    promotion_price_start_date_time: Optional[RFC3339DateTime] = Field(
        default=UNSET, alias="promotionPriceStartDateTime"
    )
    """The effective start date for a given promotion. Time should be specified in the UTC format.<br>
    promotionPriceStartDateTime is required for Create and Delete. <br><b style='color:green;'>Market availability:
    US"""

    promotion_price_end_date_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="promotionPriceEndDateTime")
    """The effective end date for a given promotion. Time should be specified in the UTC format.<br>
    promotionPriceEndDateTime is required for Create and Delete. <br><b style='color:green;'>Market availability: US"""


class PromotionInformation1Dict(TypedDict):
    promotion_setting_action: NotRequired[PromotionSettingAction1OrStr]
    promotion_placement: NotRequired[PromotionPlacementOrStr]
    promotion_type: NotRequired[PromotionType1OrStr]
    promotion_price: NotRequired[float]
    promotion_price_start_date_time: NotRequired[RFC3339DateTime]
    promotion_price_end_date_time: NotRequired[RFC3339DateTime]
