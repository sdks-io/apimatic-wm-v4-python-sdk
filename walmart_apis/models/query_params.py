from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class QueryParams(SdkBaseModel):
    return_order_id: Optional[str] = Field(default=UNSET, alias="returnOrderId")
    """Return order identifier of the return order object.<br><b style='color:green;'>Market availability: Global</b>"""

    customer_order_id: Optional[str] = Field(default=UNSET, alias="customerOrderId")
    """A unique ID associated with the sales order for specified customer.<br><b style='color:green;'>Market
    availability: Global</b>"""

    status: Optional[list[str]] = UNSET
    """The status can be specified to query returns with a specific status. Valid values will be Initiated, Completed
    and Cancelled.<br><b style='color:green;'>Market availability: Global</b>"""

    replacement_info: Optional[str] = Field(default=UNSET, alias="replacementInfo")
    """Provides additional attributes related to replacement return orders in the response, if available. These
    attributes include replacementCustomerOrderID, returnType, rechargeReason, and returnCancellationReason. Allowed
    values are true or false.<br><b style='color:green;'>Market availability: US</b>"""

    return_type: Optional[list[str]] = Field(default=UNSET, alias="returnType")
    """Filters the results to return orders with the specified return type. Possible values are PREORDER, REPLACEMENT,
    or REFUND.<br><b style='color:green;'>Market availability: US</b>"""

    return_creation_start_date: Optional[str] = Field(default=UNSET, alias="returnCreationStartDate")
    """Start date for querying all return orders created after that date. Use one of the following UTC, ISO 8601
    formats. Date example: '2013-08-16' Timestamp example: '2013-08-16T10:30:15Z'<br><b style='color:green;'>Market
    availability: Global</b>"""

    return_creation_end_date: Optional[str] = Field(default=UNSET, alias="returnCreationEndDate")
    """Limits the query to return orders created before this returnCreationEndDate. Use one of the following ISO 8601
    formats: UTC date or timestamp. Examples: '2016-08-16T10:30:30.155Z' or '2016-08-16'<br><b
    style='color:green;'>Market availability: Global</b>"""

    return_last_modified_start_date: Optional[str] = Field(default=UNSET, alias="returnLastModifiedStartDate")
    """Start Date for querying all return orders that were modified after that date. Use one of the following UTC, ISO
    8601 formats: Date example: 2013-08-16, Timestamp example: 2013-08-16T10:30:15Z For dates with timezone, use the
    format 2020-04-17T10:42:41.000+0000 and encode '+' as %20.<br><b style='color:green;'>Market availability: US</b>"""

    return_last_modified_end_date: Optional[str] = Field(default=UNSET, alias="returnLastModifiedEndDate")
    """Limits the query to the return orders that were modified before this date. Use one of the following UTC, ISO 8601
    formats: Date example: 2013-08-16, Timestamp example: 2013-08-18T10:30:15Z For dates with timezone, use the format
    2020-04-18T10:42:41.000+0000 and encode '+' as %20.<br><b style='color:green;'>Market availability: US</b>"""

    limit: Optional[int] = UNSET
    """The number of orders to be returned. Cannot be larger than 200.<br><b style='color:green;'>Market availability:
    Global</b>"""

    is_wfs_enabled: Optional[str] = Field(default=UNSET, alias="isWFSEnabled")
    """Flag to get WFS returns. Valid value is Y.<br><b style='color:green;'>Market availability: MX | CA | CL</b>"""

    offset: Optional[int] = UNSET
    """The starting offset of the first order required in the response. Cannot be greater than 1000.<br><b
    style='color:green;'>Market availability: MX | CA | CL</b>"""

    seller_id: Optional[str] = Field(default=UNSET, alias="sellerId")
    """Unique ID of the Seller.<br><b style='color:green;'>Market availability: US</b>"""


class QueryParamsDict(TypedDict):
    return_order_id: NotRequired[str]
    customer_order_id: NotRequired[str]
    status: NotRequired[list[str]]
    replacement_info: NotRequired[str]
    return_type: NotRequired[list[str]]
    return_creation_start_date: NotRequired[str]
    return_creation_end_date: NotRequired[str]
    return_last_modified_start_date: NotRequired[str]
    return_last_modified_end_date: NotRequired[str]
    limit: NotRequired[int]
    is_wfs_enabled: NotRequired[str]
    offset: NotRequired[int]
    seller_id: NotRequired[str]
