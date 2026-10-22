from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Carrier1(SdkBaseModel):
    """carriers"""

    carrier_id: Optional[str] = Field(default=UNSET, alias="carrierId")
    """The carrier ID. A unique identifier for the carrier.

    <b style="color: green;">Market availability: Global</b>"""

    short_name: Optional[str] = Field(default=UNSET, alias="shortName")
    """The carrier's short name.

    <b style="color: green;">Market availability: Global</b>"""

    carrier_name: Optional[str] = Field(default=UNSET, alias="carrierName")
    """The carrier's name.

    <b style="color: green;">Market availability: Global</b>"""


class Carrier1Dict(TypedDict):
    carrier_id: NotRequired[str]
    short_name: NotRequired[str]
    carrier_name: NotRequired[str]
