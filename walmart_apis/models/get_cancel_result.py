from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_cancel_result_payload import GetCancelResultPayload, GetCancelResultPayloadDict


class GetCancelResult(SdkBaseModel):
    payload: Optional[GetCancelResultPayload] = UNSET
    status: Optional[str] = UNSET


class GetCancelResultDict(TypedDict):
    payload: NotRequired[GetCancelResultPayloadDict]
    status: NotRequired[str]
