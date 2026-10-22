from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MetaDataRequest(SdkBaseModel):
    """Meta information for the request."""

    limit: int = 200
    """Number of records expected in the request
     Limit for US is 1 to 200 <br>Limit for CA and MX is 1 to 1000 <br>Default is 200"""

    next_cursor: Optional[str] = Field(default=UNSET, alias="nextCursor")
    """Used for pagination when more than 200 records are retrieved. The nextCursor value of the response includes a
    marker which needs to be passed in next call which retrieves the next page of results."""


class MetaDataRequestDict(TypedDict):
    limit: NotRequired[int]
    next_cursor: NotRequired[str]
