from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class StateDto(SdkBaseModel):
    """State configuration to which shipping has to be covered with added carriers as part of mentioned sub region
    area."""

    state_code: Optional[str] = Field(default=UNSET, alias="stateCode")
    """State code for covered shipping."""

    state_name: Optional[str] = Field(default=UNSET, alias="stateName")
    """State name for covered shipping."""


class StateDtoDict(TypedDict):
    state_code: NotRequired[str]
    state_name: NotRequired[str]
