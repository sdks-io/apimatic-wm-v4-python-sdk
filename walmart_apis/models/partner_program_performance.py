from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PartnerProgramPerformance(SdkBaseModel):
    refund_rate_seller_fault: Optional[float] = Field(default=UNSET, alias="refundRateSellerFault")
    refund_rate_customer_fault: Optional[float] = Field(default=UNSET, alias="refundRateCustomerFault")
    ots: Optional[float] = UNSET
    otd: Optional[float] = UNSET
    vtr: Optional[float] = UNSET
    cancellation_seller_fault: Optional[float] = Field(default=UNSET, alias="cancellationSellerFault")
    cancellation_customer_fault: Optional[float] = Field(default=UNSET, alias="cancellationCustomerFault")


class PartnerProgramPerformanceDict(TypedDict):
    refund_rate_seller_fault: NotRequired[float]
    refund_rate_customer_fault: NotRequired[float]
    ots: NotRequired[float]
    otd: NotRequired[float]
    vtr: NotRequired[float]
    cancellation_seller_fault: NotRequired[float]
    cancellation_customer_fault: NotRequired[float]
