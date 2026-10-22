from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PartnerProgramAccSummary(SdkBaseModel):
    opening_balance: Optional[float] = Field(default=UNSET, alias="openingBalance")
    order_activity: Optional[float] = Field(default=UNSET, alias="orderActivity")
    walmart_fulfillment_services: Optional[float] = Field(default=UNSET, alias="walmartFulfillmentServices")
    other_activities: Optional[float] = Field(default=UNSET, alias="otherActivities")
    reserve: Optional[float] = UNSET
    paid_to_you: Optional[float] = Field(default=UNSET, alias="paidToYou")
    closing_balance: Optional[float] = Field(default=UNSET, alias="closingBalance")
    scheduled_settlement_date: Optional[str] = Field(default=UNSET, alias="scheduledSettlementDate")
    payment_processor: Optional[str] = Field(default=UNSET, alias="paymentProcessor")
    settle_cycle: Optional[str] = Field(default=UNSET, alias="settleCycle")
    reserve_to_date: Optional[float] = Field(default=UNSET, alias="reserveToDate")
    last_updated_date: Optional[str] = Field(default=UNSET, alias="lastUpdatedDate")
    hold_amt: Optional[float] = Field(default=UNSET, alias="holdAmt")
    hold_dates: Optional[str] = Field(default=UNSET, alias="holdDates")


class PartnerProgramAccSummaryDict(TypedDict):
    opening_balance: NotRequired[float]
    order_activity: NotRequired[float]
    walmart_fulfillment_services: NotRequired[float]
    other_activities: NotRequired[float]
    reserve: NotRequired[float]
    paid_to_you: NotRequired[float]
    closing_balance: NotRequired[float]
    scheduled_settlement_date: NotRequired[str]
    payment_processor: NotRequired[str]
    settle_cycle: NotRequired[str]
    reserve_to_date: NotRequired[float]
    last_updated_date: NotRequired[str]
    hold_amt: NotRequired[float]
    hold_dates: NotRequired[str]
