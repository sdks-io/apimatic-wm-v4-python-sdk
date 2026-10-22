from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload2 import Payload2, Payload2Dict


class GetUnpublishedItemsCount(SdkBaseModel):
    payload: Optional[list[Payload2]] = UNSET


class GetUnpublishedItemsCountDict(TypedDict):
    payload: NotRequired[list[Payload2Dict]]
