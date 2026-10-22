from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Meta1(SdkBaseModel):
    total_count: Optional[int] = Field(default=UNSET, alias="totalCount")
    """Total no of return orders.<br><b style='color:green;'>Market availability: Global</b>"""

    limit: Optional[int] = UNSET
    """The number of orders to be returned.<br><b style='color:green;'>Market availability: Global</b>"""

    next_cursor_mark: Optional[str] = Field(default=UNSET, alias="nextCursorMark")
    """String to be used as query parameter for getting next set of return orders.<br><b style='color:green;'>Market
    availability: Global</b>"""


class Meta1Dict(TypedDict):
    total_count: NotRequired[int]
    limit: NotRequired[int]
    next_cursor_mark: NotRequired[str]
