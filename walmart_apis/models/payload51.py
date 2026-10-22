from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.item_status10 import ItemStatus10OrStr


class Payload51(SdkBaseModel):
    """Response payload."""

    item_status: Optional[ItemStatus10OrStr] = Field(default=UNSET, alias="itemStatus")
    """IRP status of the items.<br><b style='color:green;'>Market availability: US only</b>"""

    categories: Optional[list[str]] = UNSET
    """The Category of the items in requested item status.<br><b style='color:green;'>Market availability: US
    only</b>"""


class Payload51Dict(TypedDict):
    item_status: NotRequired[ItemStatus10OrStr]
    categories: NotRequired[list[str]]
