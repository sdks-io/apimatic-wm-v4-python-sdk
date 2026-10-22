from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .partner_program_statement_do import PartnerProgramStatementDo, PartnerProgramStatementDoDict


class PartnerProgramStatementRes(SdkBaseModel):
    status_code: Optional[int] = Field(default=UNSET, alias="statusCode")
    status: Optional[str] = UNSET
    error: Optional[str] = UNSET
    partner_id: Optional[str] = Field(default=UNSET, alias="partnerId")
    payload: Optional[PartnerProgramStatementDo] = UNSET


class PartnerProgramStatementResDict(TypedDict):
    status_code: NotRequired[int]
    status: NotRequired[str]
    error: NotRequired[str]
    partner_id: NotRequired[str]
    payload: NotRequired[PartnerProgramStatementDoDict]
