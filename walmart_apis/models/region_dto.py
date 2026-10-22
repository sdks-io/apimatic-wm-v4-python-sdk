from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sub_region_dto import SubRegionDto, SubRegionDtoDict


class RegionDto(SdkBaseModel):
    """Region configurations to which shipping has to be covered with added carriers."""

    region_code: Optional[str] = Field(default=UNSET, alias="regionCode")
    """Region code for covered shipping."""

    region_name: Optional[str] = Field(default=UNSET, alias="regionName")
    """Region name for covered shipping."""

    sub_regions: Optional[list[SubRegionDto]] = Field(default=UNSET, alias="subRegions")
    """Sub region configurations to which shipping has to be covered with added carriers."""


class RegionDtoDict(TypedDict):
    region_code: NotRequired[str]
    region_name: NotRequired[str]
    sub_regions: NotRequired[list[SubRegionDtoDict]]
