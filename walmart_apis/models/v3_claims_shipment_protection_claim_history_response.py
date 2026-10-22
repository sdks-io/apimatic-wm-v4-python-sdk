from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data import Data, DataDict


class V3ClaimsShipmentProtectionClaimHistoryResponse(SdkBaseModel):
    data: Optional[Data] = UNSET


class V3ClaimsShipmentProtectionClaimHistoryResponseDict(TypedDict):
    data: NotRequired[DataDict]
