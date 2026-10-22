from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .state_dto import StateDto, StateDtoDict


class SubRegionDto(SdkBaseModel):
    """Sub region configurations to which shipping has to be covered with added carriers."""

    sub_region_code: Optional[str] = Field(default=UNSET, alias="subRegionCode")
    """Sub region code for covered shipping."""

    sub_region_name: Optional[str] = Field(default=UNSET, alias="subRegionName")
    """Sub region name for covered shipping."""

    states: Optional[list[StateDto]] = UNSET
    """State configuration to which shipping has to be covered with added carriers as part of mentioned sub region
    area."""


class SubRegionDtoDict(TypedDict):
    sub_region_code: NotRequired[str]
    sub_region_name: NotRequired[str]
    states: NotRequired[list[StateDtoDict]]
