from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_vtr_result_payload import GetVtrResultPayload, GetVtrResultPayloadDict


class GetVtrResult(SdkBaseModel):
    payload: Optional[GetVtrResultPayload] = UNSET
    status: Optional[str] = UNSET


class GetVtrResultDict(TypedDict):
    payload: NotRequired[GetVtrResultPayloadDict]
    status: NotRequired[str]
