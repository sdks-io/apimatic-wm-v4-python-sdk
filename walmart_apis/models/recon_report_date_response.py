from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReconReportDateResponse(SdkBaseModel):
    available_ap_report_dates: Optional[list[str]] = Field(default=UNSET, alias="availableApReportDates")
    """All available report dates are returned"""


class ReconReportDateResponseDict(TypedDict):
    available_ap_report_dates: NotRequired[list[str]]
