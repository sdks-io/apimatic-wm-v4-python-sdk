from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .headers import Headers, HeadersDict
from .payload8 import Payload8, Payload8Dict


class WfsInventoryDto(SdkBaseModel):
    headers: Optional[Headers] = UNSET
    payload: Optional[Payload8] = UNSET


class WfsInventoryDtoDict(TypedDict):
    headers: NotRequired[HeadersDict]
    payload: NotRequired[Payload8Dict]
