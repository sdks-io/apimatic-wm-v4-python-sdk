from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.parameter import ParameterOrStr
from .enums.values import ValuesOrStr


class EnumFilter(SdkBaseModel):
    """Filter based on preset parameters and their associated values is possible with EnumFilter. No parameter should be
    repeated."""

    parameter: Optional[ParameterOrStr] = UNSET
    """Used to apply an enum filter based on a predefined parameter.

    | Attribute | Description | Data Type |
    | --- | --- | --- |
    | ITEM_AVAILABILITY_STATUS | Filters items based on whether they are new to Walmart or already exist on Walmart. |
        string |
    | DEMAND_SALES_TRENDS | Indicates the months of the year when high demand is observed for the recommended item. |
        string |"""

    values: Optional[ValuesOrStr] = UNSET
    """Predefined values used to apply filters to the response. Multiple values are evaluated using the OR operator.

    | Attribute | Associated parameter of enumFilter | Description | Data Type |
    | --- | --- | --- | --- |
    | EXISTING_IN_WALMART | ITEM_AVAILABILITY_STATUS | Filters items that already exist on Walmart. | string |
    | NEW_TO_WALMART | ITEM_AVAILABILITY_STATUS | Filters items that are new to Walmart. | string |
    | JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC | DEMAND_SALES_TRENDS | Indicates the months of the
        year when high demand is observed for the recommended item. | string |"""


class EnumFilterDict(TypedDict):
    parameter: NotRequired[ParameterOrStr]
    values: NotRequired[ValuesOrStr]
