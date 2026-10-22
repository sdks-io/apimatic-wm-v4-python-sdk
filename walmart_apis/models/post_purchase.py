from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cancellations import Cancellations, CancellationsDict


class PostPurchase(SdkBaseModel):
    cancellations: Optional[Cancellations] = UNSET
    returns: Optional[Any] = UNSET
    issue_count: Optional[str] = Field(default=UNSET, alias="issueCount")
    otd: Optional[Cancellations] = UNSET


class PostPurchaseDict(TypedDict):
    cancellations: NotRequired[CancellationsDict]
    returns: NotRequired[Any]
    issue_count: NotRequired[str]
    otd: NotRequired[CancellationsDict]
