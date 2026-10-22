from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .report_error import ReportError, ReportErrorDict


class V3ReportReconreportReconFile400Error(SdkBaseModel):
    error: Optional[list[ReportError]] = UNSET


class V3ReportReconreportReconFile400ErrorDict(TypedDict):
    error: NotRequired[list[ReportErrorDict]]
