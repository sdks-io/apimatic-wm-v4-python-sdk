from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V3ReportsSchedulesRequest(SdkBaseModel):
    repeats_every: Optional[float] = Field(default=UNSET, alias="repeatsEvery")
    """Defines the interval at which the report repeats based on the selected frequency."""

    hour: Optional[float] = UNSET
    """Specifies the hour of the day at which the schedule will be triggered. Allowed values are from 0 to 23, where 0
    corresponds to 12:00 AM UTC and 23 corresponds to 11:00 PM UTC. The hour selection is based on the UTC timezone."""

    day_of_month: Optional[float] = Field(default=UNSET, alias="dayOfMonth")
    """Specifies the day of the month on which the schedule will be triggered."""

    day_of_week: Optional[float] = Field(default=UNSET, alias="dayOfWeek")
    """Specifies the day of the week on which the schedule will be triggered. Allowed values are from 0 to 6, where 0
    represents Monday and 6 represents Sunday."""

    month_of_year: Optional[float] = Field(default=UNSET, alias="monthOfYear")
    """Specifies the month in which the schedule will be triggered. Allowed values are from 1 to 12."""

    schedule_start_date: Optional[str] = Field(default=UNSET, alias="scheduleStartDate")
    """Specifies the start date for the schedule. The date should be in a valid date format (Example: YYYY-MM-DD)."""


class V3ReportsSchedulesRequestDict(TypedDict):
    repeats_every: NotRequired[float]
    hour: NotRequired[float]
    day_of_month: NotRequired[float]
    day_of_week: NotRequired[float]
    month_of_year: NotRequired[float]
    schedule_start_date: NotRequired[str]
