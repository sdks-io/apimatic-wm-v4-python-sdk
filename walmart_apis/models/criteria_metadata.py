from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CriteriaMetadata(SdkBaseModel):
    """Specifies the metadata value for each criterion<br><b style='color:green;'>Market availability: US only</b>"""

    orders: Optional[float] = UNSET
    """Specifies number of orders received in the given timeframe.<br><b style='color:green;'>Market availability: US |
    CA</b>"""

    active_days: Optional[float] = Field(default=UNSET, alias="activeDays")
    """Specifies the number of days the seller has been active on the platform.<br><b style='color:green;'>Market
    availability: US | CA</b>"""

    on_time_delivery_rate: Optional[float] = Field(default=UNSET, alias="onTimeDeliveryRate")
    """Specifies the on-time delivery rate within the given timeframe.<br><b style='color:green;'>Market availability:
    US | CA</b>"""

    cancellation_rate: Optional[float] = Field(default=UNSET, alias="cancellationRate")
    """Specifies the cancellation rate within the given timeframe.<br><b style='color:green;'>Market availability: US |
    CA</b>"""

    seller_response_rate: Optional[float] = Field(default=UNSET, alias="sellerResponseRate")
    """Specifies the seller's response rate.<br><b style='color:green;'>Market availability: US | CA</b>"""

    shipping_score: Optional[float] = Field(default=UNSET, alias="shippingScore")
    """Specifies the seller's shipping score.<br><b style='color:green;'>Market availability: US only</b>"""

    content_score: Optional[float] = Field(default=UNSET, alias="contentScore")
    """Specifies the seller's content score.<br><b style='color:green;'>Market availability: US | CA</b>"""

    price_mb_score: Optional[float] = Field(default=UNSET, alias="priceMbScore")
    """Specifies the seller's meet or beat score.<br><b style='color:green;'>Market availability: US | CA</b>"""

    promise_accuracy: Optional[float] = Field(default=UNSET, alias="promiseAccuracy")
    """Specifies the difference between the promised and actual delivery dates.<br><b style='color:green;'>Market
    availability: CA only</b>"""


class CriteriaMetadataDict(TypedDict):
    orders: NotRequired[float]
    active_days: NotRequired[float]
    on_time_delivery_rate: NotRequired[float]
    cancellation_rate: NotRequired[float]
    seller_response_rate: NotRequired[float]
    shipping_score: NotRequired[float]
    content_score: NotRequired[float]
    price_mb_score: NotRequired[float]
    promise_accuracy: NotRequired[float]
