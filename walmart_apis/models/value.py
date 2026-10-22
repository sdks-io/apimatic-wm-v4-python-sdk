from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Value(SdkBaseModel):
    score_type: Optional[str] = Field(default=UNSET, alias="scoreType")
    score_value: Optional[int] = Field(default=UNSET, alias="scoreValue")
    impact: Optional[str] = UNSET


class ValueDict(TypedDict):
    score_type: NotRequired[str]
    score_value: NotRequired[int]
    impact: NotRequired[str]
