from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_srrresult_payload import GetSrrresultPayload, GetSrrresultPayloadDict


class GetSrrresult(SdkBaseModel):
    payload: Optional[GetSrrresultPayload] = UNSET
    status: Optional[str] = UNSET


class GetSrrresultDict(TypedDict):
    payload: NotRequired[GetSrrresultPayloadDict]
    status: NotRequired[str]
