from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_trending_result_payload import GetTrendingResultPayload, GetTrendingResultPayloadDict


class GetTrendingResult(SdkBaseModel):
    payload: Optional[GetTrendingResultPayload] = UNSET
    status: Optional[str] = UNSET


class GetTrendingResultDict(TypedDict):
    payload: NotRequired[GetTrendingResultPayloadDict]
    status: NotRequired[str]
