from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sem_invoice import SemInvoice, SemInvoiceDict
from .sem_pagination import SemPagination, SemPaginationDict


class SemBillingHistoryResponse(SdkBaseModel):
    pagination: Optional[SemPagination] = UNSET
    """Pagination details"""

    data: Optional[list[SemInvoice]] = UNSET
    """List of invoices"""


class SemBillingHistoryResponseDict(TypedDict):
    pagination: NotRequired[SemPaginationDict]
    data: NotRequired[list[SemInvoiceDict]]
