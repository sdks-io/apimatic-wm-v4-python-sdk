from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sem_error400 import SemError400, SemError400Dict


class V3ClaimsShipmentProtection400Error(SdkBaseModel):
    errors: Optional[list[SemError400]] = UNSET


class V3ClaimsShipmentProtection400ErrorDict(TypedDict):
    errors: NotRequired[list[SemError400Dict]]
