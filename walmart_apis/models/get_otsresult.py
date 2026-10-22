from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_otsresult_payload import GetOtsresultPayload, GetOtsresultPayloadDict


class GetOtsresult(SdkBaseModel):
    payload: Optional[GetOtsresultPayload] = UNSET
    status: Optional[str] = UNSET


class GetOtsresultDict(TypedDict):
    payload: NotRequired[GetOtsresultPayloadDict]
    status: NotRequired[str]
