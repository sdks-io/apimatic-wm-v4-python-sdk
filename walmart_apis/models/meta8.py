from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Meta8(SdkBaseModel):
    """Meta information for the response. <br><b style='color:green;'>Market availability: US only</span></b>"""

    total_records: Optional[int] = Field(default=UNSET, alias="totalRecords")
    """The total number of records are present for the requested variants based on the primary variant item ID."""

    records_fetched: Optional[int] = Field(default=UNSET, alias="recordsFetched")
    """The number of records fetched in the response."""

    limit: int = 200
    """Number of records expected in the request"""

    next_cursor: Optional[str] = Field(default=UNSET, alias="nextCursor")
    """The string returned from the initial API call to indicate nextCursor. Specify nextCursor value to retrieve the
    next set of records."""


class Meta8Dict(TypedDict):
    total_records: NotRequired[int]
    records_fetched: NotRequired[int]
    limit: NotRequired[int]
    next_cursor: NotRequired[str]
