from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .schedule import Schedule, ScheduleDict


class V3ReportsSchedulesResponse(SdkBaseModel):
    page: Optional[int] = UNSET
    """Current page"""

    total_count: Optional[int] = Field(default=UNSET, alias="totalCount")
    """Number of records fetched."""

    limit: Optional[int] = UNSET
    """Number of records to be returned. Default is 10."""

    next_cursor: Optional[str] = Field(default=UNSET, alias="nextCursor")
    """Specifies pagination when records exceed the specified limit (or default of 10); pass this parameter for the next
    API call. You only need to pass the cursor value as a query parameter, not the initial API call query parameters.
    For example, if
    ['nextCursor'='reportType=ITEM&requestStatus=ERROR&requestSubmissionStartDate=2021-08-20T10:52:59Z&requestSubmissionEndDate=2021-09-14T10:52:59Z&page=2&limit=1']
    then the subsequent call will be:
    [marketplace.walmartapis.com/v3/reports/reportRequests?reportType=ITEM&requestStatus=ERROR&requestSubmissionStartDate=2021-08-20T10:52:59Z&requestSubmissionEndDate=2021-09-14T10:52:59Z&page=2&limit=1].
    You only need to use the nextCursor value instead of the original query parameters."""

    schedules: Optional[list[Schedule]] = UNSET


class V3ReportsSchedulesResponseDict(TypedDict):
    page: NotRequired[int]
    total_count: NotRequired[int]
    limit: NotRequired[int]
    next_cursor: NotRequired[str]
    schedules: NotRequired[list[ScheduleDict]]
