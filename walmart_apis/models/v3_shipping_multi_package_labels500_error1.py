from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error71 import Error71, Error71Dict


class V3ShippingMultiPackageLabels500Error1(SdkBaseModel):
    errors: Optional[list[Error71]] = UNSET


class V3ShippingMultiPackageLabels500Error1Dict(TypedDict):
    errors: NotRequired[list[Error71Dict]]
