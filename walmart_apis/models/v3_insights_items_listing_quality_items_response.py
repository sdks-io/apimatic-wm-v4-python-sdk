from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload11 import Payload11, Payload11Dict


class V3InsightsItemsListingQualityItemsResponse(SdkBaseModel):
    next_cursor: Optional[str] = Field(default=UNSET, alias="nextCursor")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    total_items: Optional[str] = Field(default=UNSET, alias="totalItems")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    payload: Optional[list[Payload11]] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    status: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class V3InsightsItemsListingQualityItemsResponseDict(TypedDict):
    next_cursor: NotRequired[str]
    total_items: NotRequired[str]
    payload: NotRequired[list[Payload11Dict]]
    status: NotRequired[str]
