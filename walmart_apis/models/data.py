from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.current_claim_status import CurrentClaimStatusOrStr
from .history import History, HistoryDict


class Data(SdkBaseModel):
    current_claim_status: Optional[CurrentClaimStatusOrStr] = Field(default=UNSET, alias="currentClaimStatus")
    history: Optional[list[History]] = UNSET


class DataDict(TypedDict):
    current_claim_status: NotRequired[CurrentClaimStatusOrStr]
    history: NotRequired[list[HistoryDict]]
