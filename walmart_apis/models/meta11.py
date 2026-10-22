from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Meta11(SdkBaseModel):
    """Meta information for the response."""

    total_records: Optional[int] = Field(default=UNSET, alias="totalRecords")
    """The total number of records are present for the requested categorization type along with filters. <br><b
    style='color:green;'>Market availability: US | CA | MX</span></b>"""

    records_fetched: Optional[int] = Field(default=UNSET, alias="recordsFetched")
    """The number of records fetched in the response. <br><b style='color:green;'>Market availability: US | CA |
    MX</span></b>"""

    limit: int = 200
    """Number of records expected in the request
     Limit for US is 1 to 200 <br>Limit for CA and MX is 1 to 1000 <br>Default is 200 <br><b style='color:green;'>Market
        availability: US only</span></b>"""

    next_cursor: Optional[str] = Field(default=UNSET, alias="nextCursor")
    """The string returned from the initial API call to indicate nextCursor. Specify nextCursor value to retrieve the
    next set of records. <br><b style='color:green;'>Market availability: US only</span></b>"""


class Meta11Dict(TypedDict):
    total_records: NotRequired[int]
    records_fetched: NotRequired[int]
    limit: NotRequired[int]
    next_cursor: NotRequired[str]
