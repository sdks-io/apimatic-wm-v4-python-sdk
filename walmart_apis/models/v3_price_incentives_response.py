from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item1 import Item1, Item1Dict
from .page_context import PageContext, PageContextDict


class V3PriceIncentivesResponse(SdkBaseModel):
    page_context: Optional[PageContext] = Field(default=UNSET, alias="pageContext")
    """<br><b style='color:green;'>Market availability: US</b>"""

    items: Optional[list[Item1]] = UNSET
    """<br><b style='color:green;'>Market availability: US</b>"""


class V3PriceIncentivesResponseDict(TypedDict):
    page_context: NotRequired[PageContextDict]
    items: NotRequired[list[Item1Dict]]
