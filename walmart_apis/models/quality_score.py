from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .value import Value, ValueDict


class QualityScore(SdkBaseModel):
    score: Optional[float] = UNSET
    values: Optional[list[Value]] = UNSET


class QualityScoreDict(TypedDict):
    score: NotRequired[float]
    values: NotRequired[list[ValueDict]]
