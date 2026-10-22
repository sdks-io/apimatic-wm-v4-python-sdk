from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Meta12(SdkBaseModel):
    """Meta data about the list.<br><b style='color:green;'>Market availability: MX</b>"""

    total_count: Optional[int] = Field(default=UNSET, alias="totalCount")
    """Total no of return orders.<br><b style='color:green;'>Market availability: MX</b>"""

    limit: Optional[int] = UNSET
    """The number of orders to be returned.<br><b style='color:green;'>Market availability: MX</b>"""

    next_cursor_mark: Optional[str] = Field(default=UNSET, alias="nextCursorMark")
    """nextCursorMark.<br><b style='color:green;'>Market availability: MX</b>"""


class Meta12Dict(TypedDict):
    total_count: NotRequired[int]
    limit: NotRequired[int]
    next_cursor_mark: NotRequired[str]
