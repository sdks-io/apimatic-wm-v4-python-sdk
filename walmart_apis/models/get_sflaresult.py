from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_sflaresult_payload import GetSflaresultPayload, GetSflaresultPayloadDict


class GetSflaresult(SdkBaseModel):
    payload: Optional[GetSflaresultPayload] = UNSET
    status: Optional[str] = UNSET


class GetSflaresultDict(TypedDict):
    payload: NotRequired[GetSflaresultPayloadDict]
    status: NotRequired[str]
