from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta7 import Meta7, Meta7Dict
from .record4 import Record4, Record4Dict


class Payload3(SdkBaseModel):
    """Payload in the response having the details about the item recommendations."""

    recommendation_type: Literal["ITEM"] = Field(default="ITEM", alias="recommendationType")
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ITEM | To get list of recommended items | string |
    <br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""

    meta: Optional[Meta7] = UNSET
    """Meta information for the response."""

    records: Optional[list[Record4]] = UNSET
    """Information related to the item recommendations."""


class Payload3Dict(TypedDict):
    recommendation_type: Literal["ITEM"]
    meta: NotRequired[Meta7Dict]
    records: NotRequired[list[Record4Dict]]
