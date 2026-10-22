from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data8 import Data8, Data8Dict


class V3ShippingLabelsCarriersPackageTypesResponse(SdkBaseModel):
    data: Optional[list[Data8]] = UNSET
    """data

    <b style="color: green;">Market availability: Global</b>"""


class V3ShippingLabelsCarriersPackageTypesResponseDict(TypedDict):
    data: NotRequired[list[Data8Dict]]
