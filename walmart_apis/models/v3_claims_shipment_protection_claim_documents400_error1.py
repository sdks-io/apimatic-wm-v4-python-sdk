from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sem_error400 import SemError400, SemError400Dict


class V3ClaimsShipmentProtectionClaimDocuments400Error1(SdkBaseModel):
    errors: Optional[list[SemError400]] = UNSET


class V3ClaimsShipmentProtectionClaimDocuments400Error1Dict(TypedDict):
    errors: NotRequired[list[SemError400Dict]]
