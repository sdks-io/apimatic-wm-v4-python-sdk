from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Otd(SdkBaseModel):
    defected_order: Optional[int] = Field(default=UNSET, alias="defectedOrder")
    total_order: Optional[int] = Field(default=UNSET, alias="totalOrder")
    rate: Optional[int] = UNSET


class OtdDict(TypedDict):
    defected_order: NotRequired[int]
    total_order: NotRequired[int]
    rate: NotRequired[int]
