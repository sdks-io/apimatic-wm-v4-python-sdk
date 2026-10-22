from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .tax_form import TaxForm, TaxFormDict


class PaymentProcessorSummary(SdkBaseModel):
    payout_year: Optional[str] = Field(default=UNSET, alias="payoutYear")
    """Payout year for which tax forms were generated, formatted as YYYY."""

    tax_forms: Optional[list[TaxForm]] = Field(default=UNSET, alias="taxForms")
    """Tax forms available for the specified payout year."""


class PaymentProcessorSummaryDict(TypedDict):
    payout_year: NotRequired[str]
    tax_forms: NotRequired[list[TaxFormDict]]
