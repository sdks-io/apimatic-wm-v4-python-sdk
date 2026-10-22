from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .report_error import ReportError, ReportErrorDict


class ReconReportError(SdkBaseModel):
    error: Optional[list[ReportError]] = UNSET


class ReconReportErrorDict(TypedDict):
    error: NotRequired[list[ReportErrorDict]]
