from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .headers import Headers, HeadersDict
from .payload21 import Payload21, Payload21Dict


class V3FulfillmentInventoryResponse(SdkBaseModel):
    headers: Optional[Headers] = UNSET
    payload: Optional[Payload21] = UNSET


class V3FulfillmentInventoryResponseDict(TypedDict):
    headers: NotRequired[HeadersDict]
    payload: NotRequired[Payload21Dict]
