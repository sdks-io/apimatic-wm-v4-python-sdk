from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_cmaresult_payload import GetCmaresultPayload, GetCmaresultPayloadDict


class GetCmaresult(SdkBaseModel):
    payload: Optional[GetCmaresultPayload] = UNSET
    status: Optional[str] = UNSET


class GetCmaresultDict(TypedDict):
    payload: NotRequired[GetCmaresultPayloadDict]
    status: NotRequired[str]
