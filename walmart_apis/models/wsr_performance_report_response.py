from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .wsr_pagination import WsrPagination, WsrPaginationDict
from .wsr_performance_data import WsrPerformanceData, WsrPerformanceDataDict


class WsrPerformanceReportResponse(SdkBaseModel):
    """Performance report response containing aggregated metrics data and pagination info.

    **Note**: The availability of identifier fields (``adGroupId``, ``creativeId``) depends on the ``performanceBy``
    parameter used in the request."""

    data: Optional[list[WsrPerformanceData]] = UNSET
    """List of performance metrics data aggregated by the specified performance level (``CAMPAIGN``, ``ADGROUP``, or
    ``CREATIVE``).

    Empty array when no data is available for the given criteria."""

    pagination: Optional[WsrPagination] = UNSET
    """Pagination metadata for navigating through the report results.

    **Empty Response**: When no data is available, all fields will be 0."""


class WsrPerformanceReportResponseDict(TypedDict):
    data: NotRequired[list[WsrPerformanceDataDict]]
    pagination: NotRequired[WsrPaginationDict]
