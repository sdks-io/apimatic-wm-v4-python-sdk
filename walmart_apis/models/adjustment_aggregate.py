from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdjustmentAggregate(SdkBaseModel):
    net_payable: Optional[float] = Field(default=UNSET, alias="netPayable")
    dispute_settlement: Optional[float] = Field(default=UNSET, alias="disputeSettlement")
    return_ship_serv_charge: Optional[float] = Field(default=UNSET, alias="returnShipServCharge")
    return_handling_serv_charge: Optional[float] = Field(default=UNSET, alias="returnHandlingServCharge")
    fwd_shipping_service_fee: Optional[float] = Field(default=UNSET, alias="fwdShippingServiceFee")


class AdjustmentAggregateDict(TypedDict):
    net_payable: NotRequired[float]
    dispute_settlement: NotRequired[float]
    return_ship_serv_charge: NotRequired[float]
    return_handling_serv_charge: NotRequired[float]
    fwd_shipping_service_fee: NotRequired[float]
