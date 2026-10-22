from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .add_ons_response import AddOnsResponse, AddOnsResponseDict
from .estimated_rate import EstimatedRate, EstimatedRateDict


class EstimateShipmentResponse(SdkBaseModel):
    """List of estimates"""

    service_type_group_name: Optional[str] = Field(default=UNSET, alias="serviceTypeGroupName")
    """Service Type Group Name"""

    service_type_group_display_name: Optional[str] = Field(default=UNSET, alias="serviceTypeGroupDisplayName")
    """Service Type Group Display Name"""

    name: Optional[str] = UNSET
    """Carrier Service Type"""

    display_name: Optional[str] = Field(default=UNSET, alias="displayName")
    """Carrier Service Type Display Name"""

    estimated_rate: Optional[EstimatedRate] = Field(default=UNSET, alias="estimatedRate")
    """Estimated Rate"""

    delivery_date: Optional[str] = Field(default=UNSET, alias="deliveryDate")
    """Delivery Date"""

    carrier_name: Optional[str] = Field(default=UNSET, alias="carrierName")
    """Carrier Short Name"""

    carrier_display_name: Optional[str] = Field(default=UNSET, alias="carrierDisplayName")
    """Carrier Display Name"""

    is_delivery_promise_fulfilled: Optional[bool] = Field(default=UNSET, alias="isDeliveryPromiseFulfilled")
    """Delivery Promise Fulfilled"""

    add_ons: Optional[list[AddOnsResponse]] = Field(default=UNSET, alias="addOns")
    """Add Ons Response"""


class EstimateShipmentResponseDict(TypedDict):
    service_type_group_name: NotRequired[str]
    service_type_group_display_name: NotRequired[str]
    name: NotRequired[str]
    display_name: NotRequired[str]
    estimated_rate: NotRequired[EstimatedRateDict]
    delivery_date: NotRequired[str]
    carrier_name: NotRequired[str]
    carrier_display_name: NotRequired[str]
    is_delivery_promise_fulfilled: NotRequired[bool]
    add_ons: NotRequired[list[AddOnsResponseDict]]
