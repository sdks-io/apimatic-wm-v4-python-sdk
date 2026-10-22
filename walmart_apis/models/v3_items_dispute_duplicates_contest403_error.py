from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error3 import Error3, Error3Dict


class V3ItemsDisputeDuplicatesContest403Error(SdkBaseModel):
    errors: Optional[list[Error3]] = UNSET


class V3ItemsDisputeDuplicatesContest403ErrorDict(TypedDict):
    errors: NotRequired[list[Error3Dict]]
