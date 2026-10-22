from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CriteriaTier(SdkBaseModel):
    """Specifies the tier for each criterion.<br><b style='color:green;'>Market availability: US | CA</b>"""

    orders: Optional[str] = UNSET
    """Specifies the eligible tier based on number of orders.<br><b style='color:green;'>Market availability: US |
    CA</b>"""

    active_days: Optional[str] = Field(default=UNSET, alias="activeDays")
    """Specifies the eligible tier based on the number of active days.<br><b style='color:green;'>Market availability:
    US | CA</b>"""

    on_time_delivery_rate: Optional[str] = Field(default=UNSET, alias="onTimeDeliveryRate")
    """Specifies the eligible tier based on the OTD rate.<br><b style='color:green;'>Market availability: US | CA</b>"""

    cancellation_rate: Optional[str] = Field(default=UNSET, alias="cancellationRate")
    """Specifies the eligible tier based on the cancellation rate.<br><b style='color:green;'>Market availability: US |
    CA</b>"""

    seller_response_rate: Optional[str] = Field(default=UNSET, alias="sellerResponseRate")
    """Specifies the eligible tier based on the seller response.<br><b style='color:green;'>Market availability: US |
    CA</b>"""

    shipping_score: Optional[str] = Field(default=UNSET, alias="shippingScore")
    """Specifies the eligible tier based on shipping score<br><b style='color:green;'>Market availability: US
    only</b>"""

    content_score: Optional[str] = Field(default=UNSET, alias="contentScore")
    """Specifies the eligible tier based on the content score.<br><b style='color:green;'>Market availability: US |
    CA</b>"""

    price_mb_score: Optional[str] = Field(default=UNSET, alias="priceMbScore")
    """Specifies the eligible tier based on the price meet or beat score.<br><b style='color:green;'>Market
    availability: US | CA</b>"""

    promise_accuracy: Optional[float] = Field(default=UNSET, alias="promiseAccuracy")
    """Specifies the difference between the promised and the actual delivery dates.<br><b style='color:green;'>Market
    availability: CA only</b>"""


class CriteriaTierDict(TypedDict):
    orders: NotRequired[str]
    active_days: NotRequired[str]
    on_time_delivery_rate: NotRequired[str]
    cancellation_rate: NotRequired[str]
    seller_response_rate: NotRequired[str]
    shipping_score: NotRequired[str]
    content_score: NotRequired[str]
    price_mb_score: NotRequired[str]
    promise_accuracy: NotRequired[float]
