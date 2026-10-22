from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.date_granularity import DateGranularityOrStr
from .unions.row_filter1 import RowFilter1, RowFilter1Dict


class V3ReportsReportRequestsRequest(SdkBaseModel):
    """Request payload"""

    row_filters: Optional[list[RowFilter1]] = Field(default=UNSET, alias="rowFilters")
    """Specifies a set of row level filters used to narrow down data by specific reportType. Refer to the guide section
    for more details.

    <strong style="color: green;">Market availability: Global</strong>"""

    exclude_columns: Optional[list[str]] = Field(default=UNSET, alias="excludeColumns")
    """Specifies columns to exclude from a report. Note that not all reports support this filter. Refer to the guide
    section for more details.

    <strong style="color: green;">Market availability: Global</strong>"""

    data_start_time: Optional[str] = Field(default=UNSET, alias="dataStartTime")
    """Start timestamp for the report data range. Use ISO 8601 format for the date (``YYYY-MM-DDTHH:mm:ssZ``). Required
    when using ``reportType=ITEM_PERFORMANCE`` and ``reportVersion=v3``. The date range from ``dataStartTime`` to
    ``dataEndTime`` must not exceed 2 years (730 days).

    <strong style="color: green;">Market availability: Global</strong>"""

    data_end_time: Optional[str] = Field(default=UNSET, alias="dataEndTime")
    """End timestamp for the report data range. Use ISO 8601 format for the date (``YYYY-MM-DDTHH:mm:ssZ``). Required
    when using ``reportType=ITEM_PERFORMANCE`` and ``reportVersion=v3``. Must be greater than or equal to
    ``dataStartTime``.

    <strong style="color: green;">Market availability: Global</strong>"""

    date_granularity: Optional[DateGranularityOrStr] = Field(default=UNSET, alias="dateGranularity")
    """Specifies the date granularity for aggregating report data. Required when using ``reportType=ITEM_PERFORMANCE``
    and ``reportVersion=v3``. Valid values are ``DAILY``, ``WEEKLY``, ``MONTHLY``, or ``QUARTERLY``. Ignored for all
    other report types and versions.

    <strong style="color: green;">Market availability: Global</strong>"""


class V3ReportsReportRequestsRequestDict(TypedDict):
    row_filters: NotRequired[list[RowFilter1Dict]]
    exclude_columns: NotRequired[list[str]]
    data_start_time: NotRequired[str]
    data_end_time: NotRequired[str]
    date_granularity: NotRequired[DateGranularityOrStr]
