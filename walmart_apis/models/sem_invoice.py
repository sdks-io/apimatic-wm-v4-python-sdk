from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SemInvoice(SdkBaseModel):
    """List of invoices"""

    invoice_date: Optional[str] = Field(default=UNSET, alias="invoiceDate")
    """The date when the invoice was generated."""

    billing_date_from: Optional[str] = Field(default=UNSET, alias="billingDateFrom")
    """Start date of the billing period."""

    billing_date_to: Optional[str] = Field(default=UNSET, alias="billingDateTo")
    """End date of the billing period."""

    status: Optional[str] = UNSET
    """Current status of the invoice."""

    amount: Optional[float] = UNSET
    """Total amount charged in the invoice."""

    currency: Optional[str] = UNSET
    """Currency in which the invoice amount is denominated."""

    payment_mode: Optional[str] = Field(default=UNSET, alias="paymentMode")
    """Payment method used for settling the invoice."""


class SemInvoiceDict(TypedDict):
    invoice_date: NotRequired[str]
    billing_date_from: NotRequired[str]
    billing_date_to: NotRequired[str]
    status: NotRequired[str]
    amount: NotRequired[float]
    currency: NotRequired[str]
    payment_mode: NotRequired[str]
