from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .partner_program_performance import PartnerProgramPerformance, PartnerProgramPerformanceDict


class PartnerProgramPerformanceRes(SdkBaseModel):
    status_code: Optional[int] = Field(default=UNSET, alias="statusCode")
    status: Optional[str] = UNSET
    error: Optional[str] = UNSET
    partner_id: Optional[str] = Field(default=UNSET, alias="partnerId")
    day7: Optional[PartnerProgramPerformance] = Field(default=UNSET, alias="7DAY")
    day14: Optional[PartnerProgramPerformance] = Field(default=UNSET, alias="14DAY")
    day30: Optional[PartnerProgramPerformance] = Field(default=UNSET, alias="30DAY")
    day60: Optional[PartnerProgramPerformance] = Field(default=UNSET, alias="60DAY")
    day90: Optional[PartnerProgramPerformance] = Field(default=UNSET, alias="90DAY")


class PartnerProgramPerformanceResDict(TypedDict):
    status_code: NotRequired[int]
    status: NotRequired[str]
    error: NotRequired[str]
    partner_id: NotRequired[str]
    day7: NotRequired[PartnerProgramPerformanceDict]
    day14: NotRequired[PartnerProgramPerformanceDict]
    day30: NotRequired[PartnerProgramPerformanceDict]
    day60: NotRequired[PartnerProgramPerformanceDict]
    day90: NotRequired[PartnerProgramPerformanceDict]
