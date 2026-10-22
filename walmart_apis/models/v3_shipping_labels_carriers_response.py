from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .carrier1 import Carrier1, Carrier1Dict


class V3ShippingLabelsCarriersResponse(SdkBaseModel):
    carriers: Optional[list[Carrier1]] = UNSET
    """carriers

    <b style="color: green;">Market availability: Global</b>"""


class V3ShippingLabelsCarriersResponseDict(TypedDict):
    carriers: NotRequired[list[Carrier1Dict]]
