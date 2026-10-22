from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Issue1(SdkBaseModel):
    date: Optional[str] = UNSET
    publish_flag: Optional[bool] = Field(default=UNSET, alias="publishFlag")
    transactable_flag: Optional[bool] = Field(default=UNSET, alias="transactableFlag")


class Issue1Dict(TypedDict):
    date: NotRequired[str]
    publish_flag: NotRequired[bool]
    transactable_flag: NotRequired[bool]
