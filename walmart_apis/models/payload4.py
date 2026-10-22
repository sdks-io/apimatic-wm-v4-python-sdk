from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta8 import Meta8, Meta8Dict
from .record5 import Record5, Record5Dict


class Payload4(SdkBaseModel):
    """Payload in the response having the details about the item recommendations."""

    meta: Optional[Meta8] = UNSET
    """Meta information for the response. <br><b style='color:green;'>Market availability: US only</span></b>"""

    primary_variant_item_id: Optional[str] = Field(default=UNSET, alias="primaryVariantItemId")
    """Item ID of the primary variant item. <br><b style='color:green;'>Market availability: US only</span></b>"""

    records: Optional[list[Record5]] = UNSET
    """Information related to the variant recommendations based on primary variant item ID.<br><b
    style='color:green;'>Market availability: US only</span></b>"""


class Payload4Dict(TypedDict):
    meta: NotRequired[Meta8Dict]
    primary_variant_item_id: NotRequired[str]
    records: NotRequired[list[Record5Dict]]
