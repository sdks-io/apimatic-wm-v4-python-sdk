from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payment_processor_summary import PaymentProcessorSummary, PaymentProcessorSummaryDict


class Payload10(SdkBaseModel):
    partner_id: Optional[str] = Field(default=UNSET, alias="partnerId")
    """Walmart partner identifier for the seller account."""

    payment_processor_summary: Optional[list[PaymentProcessorSummary]] = Field(
        default=UNSET, alias="paymentProcessorSummary"
    )
    """List of yearly summaries with the tax forms issued for each payout year."""


class Payload10Dict(TypedDict):
    partner_id: NotRequired[str]
    payment_processor_summary: NotRequired[list[PaymentProcessorSummaryDict]]
