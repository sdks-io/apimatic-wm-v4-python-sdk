from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .request_status_response import RequestStatusResponse, RequestStatusResponseDict


class RequestsStatusResponse(SdkBaseModel):
    page: Optional[int] = UNSET
    """Current page"""

    total_count: Optional[int] = Field(default=UNSET, alias="totalCount")
    """Number of records fetched."""

    limit: Optional[int] = UNSET
    """Number of records to be returned. Default is 10."""

    next_cursor: Optional[str] = Field(default=UNSET, alias="nextCursor")
    """Used for pagination when more than specified limit (or default 10) records are found. Use this param for next API
    call. Just have to use this value as query param. Need to pass only the cursor value and not the initial API call
    query params. For e.g. if
    ['nextCursor'='reportType=ITEM&requestStatus=ERROR&requestSubmissionStartDate=2021-08-20T10:52:59Z&requestSubmissionEndDate=2021-09-14T10:52:59Z&page=2&limit=1']
    then subsequent call to will be
    [marketplace.walmartapis.com/v3/reports/reportRequests?reportType=ITEM&requestStatus=ERROR&requestSubmissionStartDate=2021-08-20T10:52:59Z&requestSubmissionEndDate=2021-09-14T10:52:59Z&page=2&limit=1].
    Just have to use nextCursor value instead of query params"""

    requests: Optional[list[RequestStatusResponse]] = UNSET
    """List of requests"""


class RequestsStatusResponseDict(TypedDict):
    page: NotRequired[int]
    total_count: NotRequired[int]
    limit: NotRequired[int]
    next_cursor: NotRequired[str]
    requests: NotRequired[list[RequestStatusResponseDict]]
