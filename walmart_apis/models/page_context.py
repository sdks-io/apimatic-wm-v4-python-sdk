from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PageContext(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US</b>"""

    page_no: Optional[int] = Field(default=UNSET, alias="pageNo")
    """<br><b style='color:green;'>Market availability: US</b>"""

    current_page_count: Optional[int] = Field(default=UNSET, alias="currentPageCount")
    """<br><b style='color:green;'>Market availability: US</b>"""

    total_count: Optional[int] = Field(default=UNSET, alias="totalCount")
    """<br><b style='color:green;'>Market availability: US</b>"""

    total_pages: Optional[int] = Field(default=UNSET, alias="totalPages")
    """<br><b style='color:green;'>Market availability: US</b>"""


class PageContextDict(TypedDict):
    page_no: NotRequired[int]
    current_page_count: NotRequired[int]
    total_count: NotRequired[int]
    total_pages: NotRequired[int]
