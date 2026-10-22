from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .carrier import Carrier, CarrierDict
from .error31 import Error31, Error31Dict


class CarrierCommonResponseListCarrierResponse(SdkBaseModel):
    carriers: Optional[list[Carrier]] = UNSET
    """carriers"""

    errors: Optional[list[Error31]] = UNSET
    """List of error details describing why the request failed."""


class CarrierCommonResponseListCarrierResponseDict(TypedDict):
    carriers: NotRequired[list[CarrierDict]]
    errors: NotRequired[list[Error31Dict]]
