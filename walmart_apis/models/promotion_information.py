from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.promotion_setting_action import PromotionSettingActionOrStr
from .enums.promotion_type import PromotionTypeOrStr


class PromotionInformation(SdkBaseModel):
    promotion_setting_action: PromotionSettingActionOrStr = Field(alias="promotionSettingAction")
    """| Market | Translation |
    | --- | ----------- |
    | CA | ["Create", "Delete","Replace All"]|
    | MX & CL | ["Crear", "Eliminar","Reemplazar todo"]|

    <br><b style='color:green;'>Market availability: CA | MX | CL"""

    promotion_type: PromotionTypeOrStr = Field(alias="promotionType")
    """| Market | Translation |
    | --- | ----------- |
    | CA | ["Clearance", "Reduced"]|
    | MX | ["Rebaja", "Liquidación"]|

    <br><b style='color:green;'>Market availability: US | CA | MX </b>"""

    promotion_price: Optional[float] = Field(default=UNSET, alias="promotionPrice")
    """Promotion price that you want to set for the SKU.<br> promotionPrice is required for Create.<br><b
    style='color:green;'>Market availability: CA | MX | CL"""

    promotion_price_start_date_time: Optional[RFC3339DateTime] = Field(
        default=UNSET, alias="promotionPriceStartDateTime"
    )
    """The effective start date for a given promotion. Time should be specified in the UTC format.<br>
    promotionPriceStartDateTime is required for Create and Delete. <br><b style='color:green;'>Market availability: CA |
    MX | CL"""

    promotion_price_end_date_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="promotionPriceEndDateTime")
    """The effective end date for a given promotion. Time should be specified in the UTC format.<br>
    promotionPriceEndDateTime is required for Create and Delete. <br><b style='color:green;'>Market availability: CA |
    MX | CL"""


class PromotionInformationDict(TypedDict):
    promotion_setting_action: PromotionSettingActionOrStr
    promotion_type: PromotionTypeOrStr
    promotion_price: NotRequired[float]
    promotion_price_start_date_time: NotRequired[RFC3339DateTime]
    promotion_price_end_date_time: NotRequired[RFC3339DateTime]
