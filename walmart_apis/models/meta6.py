from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Meta6(SdkBaseModel):
    """Meta information for the request."""

    limit: int = 200
    """Number of records expected in the request
     limit for US is 1 to 200 and limit for CA and MX is 1 to 1000 default is 200 <br><b style='color:green;'>Market
        availability: US | CA | MX</span></b>"""

    next_cursor: Optional[str] = Field(default=UNSET, alias="nextCursor")
    """Used for pagination when more than 200 records are retrieved. The nextCursor value of the response includes a
    marker which needs to be passed in next call which retrieves the next page of results. <br><b
    style='color:green;'>Market availability: US only</span></b>"""


class Meta6Dict(TypedDict):
    limit: NotRequired[int]
    next_cursor: NotRequired[str]
