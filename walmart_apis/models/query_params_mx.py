from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class QueryParamsMx(SdkBaseModel):
    return_order_id: Optional[str] = Field(default=UNSET, alias="returnOrderId")
    """Return order identifier of the return order object as part of an array. This is the same as RMA number.<br><b
    style='color:green;'>Market availability: MX</b>"""

    customer_order_id: Optional[str] = Field(default=UNSET, alias="customerOrderId")
    """A unique ID associated with the sales order for the specified customer.<br><b style='color:green;'>Market
    availability: MX</b>"""

    return_creation_start_date: Optional[str] = Field(default=UNSET, alias="returnCreationStartDate")
    """Start Date for querying all return orders that were created after that date. Use one of the following UTC, ISO
    8601 formats: Date example: 2013-08-16, Timestamp example: 2013-08-18T10:30:15Z For dates with timezone, use the
    format 2020-04-18T10:42:41.000+0000 and encode '+' as %20.<br><b style='color:green;'>Market availability: MX</b>"""

    return_creation_end_date: Optional[str] = Field(default=UNSET, alias="returnCreationEndDate")
    """Limits the query to the return orders that were created before this returnCreationEndDate. Use one of the
    following UTC, ISO 8601 formats: Date example: 2013-08-16, Timestamp example: 2013-08-18T10:30:15Z For dates with
    timezone, use the format 2020-04-18T10:42:41.000+0000 and encode '+' as %20.<br><b style='color:green;'>Market
    availability: MX</b>"""

    status: Optional[list[str]] = UNSET
    """The status can be specified to query returns with a specific status. Valid values will be Initiated, Completed
    and Cancelled.<br><b style='color:green;'>Market availability: MX</b>"""

    limit: Optional[int] = UNSET
    """The number of orders to be returned. Cannot be larger than 200.<br><b style='color:green;'>Market availability:
    MX</b>"""

    is_wfs_enabled: Optional[str] = Field(default=UNSET, alias="isWFSEnabled")
    """Flag to get WFS returns. Valid value is Y.<br><b style='color:green;'>Market availability: MX</b>"""

    cursor_mark: Optional[str] = Field(default=UNSET, alias="cursorMark")
    """The cursor from which the next set of records will be retrieved.<br><b style='color:green;'>Market availability:
    MX</b>"""


class QueryParamsMxDict(TypedDict):
    return_order_id: NotRequired[str]
    customer_order_id: NotRequired[str]
    return_creation_start_date: NotRequired[str]
    return_creation_end_date: NotRequired[str]
    status: NotRequired[list[str]]
    limit: NotRequired[int]
    is_wfs_enabled: NotRequired[str]
    cursor_mark: NotRequired[str]
