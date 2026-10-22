from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload16 import Payload16, Payload16Dict


class V3InsightsItemsListingQualityCountResponse(SdkBaseModel):
    payload: Optional[list[Payload16]] = UNSET


class V3InsightsItemsListingQualityCountResponseDict(TypedDict):
    payload: NotRequired[list[Payload16Dict]]
