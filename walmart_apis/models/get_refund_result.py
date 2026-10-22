from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_refund_result_payload import GetRefundResultPayload, GetRefundResultPayloadDict


class GetRefundResult(SdkBaseModel):
    payload: Optional[GetRefundResultPayload] = UNSET
    status: Optional[str] = UNSET


class GetRefundResultDict(TypedDict):
    payload: NotRequired[GetRefundResultPayloadDict]
    status: NotRequired[str]
