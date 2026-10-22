from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.report_type11 import ReportType11OrStr
from .payload61 import Payload61, Payload61Dict


class Schedule(SdkBaseModel):
    schedule_id: Optional[str] = Field(default=UNSET, alias="scheduleId")
    """Unique identifier for the schedule."""

    request_submission_date: Optional[str] = Field(default=UNSET, alias="requestSubmissionDate")
    """The timestamp (date and time) indicating when the report request was submitted."""

    report_type: Optional[ReportType11OrStr] = Field(default=UNSET, alias="reportType")
    """Specifies the type of report to be generated. Example: ITEM for Item Report."""

    report_version: Optional[str] = Field(default=UNSET, alias="reportVersion")
    """Specifies the version of report for which the request is created. Example: v1."""

    report_summary: Optional[str] = Field(default=UNSET, alias="reportSummary")
    """Provides a brief summary of the report."""

    schedule_start_date: Optional[str] = Field(default=UNSET, alias="scheduleStartDate")
    """Specifies the start date for the schedule. The date should be in a valid date format (Example: YYYY-MM-DD)."""

    next_scheduled_time: Optional[str] = Field(default=UNSET, alias="nextScheduledTime")
    """The next scheduled time for the report."""

    payload: Optional[Payload61] = UNSET
    request_modified_time: Optional[str] = Field(default=UNSET, alias="requestModifiedTime")
    """The date and time when the report schedule was last modified."""


class ScheduleDict(TypedDict):
    schedule_id: NotRequired[str]
    request_submission_date: NotRequired[str]
    report_type: NotRequired[ReportType11OrStr]
    report_version: NotRequired[str]
    report_summary: NotRequired[str]
    schedule_start_date: NotRequired[str]
    next_scheduled_time: NotRequired[str]
    payload: NotRequired[Payload61Dict]
    request_modified_time: NotRequired[str]
