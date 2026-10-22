from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_otdresult_payload import GetOtdresultPayload, GetOtdresultPayloadDict


class GetOtdresult(SdkBaseModel):
    payload: Optional[GetOtdresultPayload] = UNSET
    status: Optional[str] = UNSET


class GetOtdresultDict(TypedDict):
    payload: NotRequired[GetOtdresultPayloadDict]
    status: NotRequired[str]
