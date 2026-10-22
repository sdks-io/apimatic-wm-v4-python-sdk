from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.rebate_type import RebateTypeOrStr
from .money_type import MoneyType, MoneyTypeDict


class Rebate(SdkBaseModel):
    rebate_amt: MoneyType = Field(alias="rebateAmt")
    info_url: Optional[str] = Field(default=UNSET, alias="infoUrl")
    rebate_type: Optional[RebateTypeOrStr] = Field(default=UNSET, alias="rebateType")
    start_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="startDate")
    end_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="endDate")


class RebateDict(TypedDict):
    rebate_amt: MoneyTypeDict
    info_url: NotRequired[str]
    rebate_type: NotRequired[RebateTypeOrStr]
    start_date: NotRequired[RFC3339DateTime]
    end_date: NotRequired[RFC3339DateTime]
