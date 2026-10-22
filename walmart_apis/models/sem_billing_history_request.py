from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sem_page import SemPage, SemPageDict


class SemBillingHistoryRequest(SdkBaseModel):
    page: Optional[SemPage] = UNSET
    """Pagination criteria"""


class SemBillingHistoryRequestDict(TypedDict):
    page: NotRequired[SemPageDict]
