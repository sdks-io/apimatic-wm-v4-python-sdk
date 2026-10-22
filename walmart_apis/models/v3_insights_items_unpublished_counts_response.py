from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload19 import Payload19, Payload19Dict


class V3InsightsItemsUnpublishedCountsResponse(SdkBaseModel):
    payload: Optional[list[Payload19]] = UNSET


class V3InsightsItemsUnpublishedCountsResponseDict(TypedDict):
    payload: NotRequired[list[Payload19Dict]]
