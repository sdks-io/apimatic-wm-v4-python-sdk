from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.row_filter1 import RowFilter1, RowFilter1Dict


class GenerateReportPayload(SdkBaseModel):
    """Request Payload"""

    row_filters: Optional[list[RowFilter1]] = Field(default=UNSET, alias="rowFilters")
    """Row Level filters"""

    exclude_columns: Optional[list[str]] = Field(default=UNSET, alias="excludeColumns")
    """Columns to exclude from report."""

    data_start_time: Optional[str] = Field(default=UNSET, alias="dataStartTime")
    """Start timestamp of the report date range."""

    data_end_time: Optional[str] = Field(default=UNSET, alias="dataEndTime")
    """End timestamp of the report date range."""


class GenerateReportPayloadDict(TypedDict):
    row_filters: NotRequired[list[RowFilter1Dict]]
    exclude_columns: NotRequired[list[str]]
    data_start_time: NotRequired[str]
    data_end_time: NotRequired[str]
