from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .enums.performance_by import PerformanceBy, PerformanceByOrStr
from .wsr_filter import WsrFilter, WsrFilterDict
from .wsr_page import WsrPage, WsrPageDict
from .wsr_sort import WsrSort, WsrSortDict


class WsrReportRequest(SdkBaseModel):
    """Request DTO for fetching campaign performance reports and item performance reports.

    **Required Fields**: ``startDate``, ``endDate`` **Optional Fields**: ``performanceBy`` (defaults to ``CREATIVE``),
    ``page``, ``sort``, ``filters``"""

    performance_by: PerformanceByOrStr = Field(default=PerformanceBy.CREATIVE, alias="performanceBy")
    """Aggregation level for metrics. Determines which identifier fields are populated in response.

    - **CAMPAIGN**: Only ``campaignId`` populated (``adGroupId``, ``creativeId`` will be null)
    - **ADGROUP**: ``campaignId`` and ``adGroupId`` populated (``creativeId`` will be null)
    - **CREATIVE**: All IDs populated (``campaignId``, ``adGroupId``, ``creativeId``)

    **Default**: ``CREATIVE`` (when not specified)"""

    start_date: Date = Field(alias="startDate")
    """Report start date in ISO format (YYYY-MM-DD).

    **Required**: Yes **Validation**: Must be a valid date in ISO format"""

    end_date: Date = Field(alias="endDate")
    """Report end date in ISO format (YYYY-MM-DD).

    **Required**: Yes **Validation**:
    - Must be strictly after startDate (not equal)
    - Duration between startDate and endDate must be less than 1 year"""

    page: Optional[WsrPage] = UNSET
    """Pagination configuration for controlling result set size and navigation.

    The pagination uses offset-based navigation where:
    - ``offset`` = starting record position (0-indexed)
    - ``limit`` = number of records per page

    **Internal Conversion**: pageNumber = (offset / limit) + 1"""

    sort: Optional[WsrSort] = UNSET
    """Sort configuration for ordering the report results.

    **Defaults**: field="gmv", order="DESC"
    """

    filters: Optional[list[WsrFilter]] = UNSET
    """List of filters to apply on the report. Multiple filters can be combined for more specific queries."""


class WsrReportRequestDict(TypedDict):
    performance_by: NotRequired[PerformanceByOrStr]
    start_date: Date
    end_date: Date
    page: NotRequired[WsrPageDict]
    sort: NotRequired[WsrSortDict]
    filters: NotRequired[list[WsrFilterDict]]
