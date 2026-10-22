from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.parameter4 import Parameter4OrStr
from .enums.values1 import Values1OrStr


class EnumFilter1(SdkBaseModel):
    """Filter based on preset parameters and their associated values is possible with EnumFilter. No parameter should be
    repeated."""

    parameter: Optional[Parameter4OrStr] = UNSET
    """To apply an enum filter based on the predefined parameter.

    | Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ITEM_AVAILABILITY_STATUS | To filter based on whether the items which are new to Walmart or existing in Walmart. |
        string |
    | DEMAND_SALES_TRENDS | Indicates the months of the year when high demand is observed for the recommended item. |
        string |"""

    values: Optional[Values1OrStr] = UNSET
    """Values correspond to the parameter for applying filter on the response. The data in values[] are predefined. OR
    operator is used between the values.

    | Attribute | Associated parameter of enumFilter | Description | Data Type |
    | --- | ----------- | ----------- | ------- |
    | EXISTING_IN_WALMART | ITEM_AVAILABILITY_STATUS | Filters existing items at Walmart. | string |
    | NEW_TO_WALMART | ITEM_AVAILABILITY_STATUS | Filters new items at Walmart. | string |
    | JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC | DEMAND_SALES_TRENDS | Indicates the months of the
        year when high demand is observed for the recommended item. | string |"""


class EnumFilter1Dict(TypedDict):
    parameter: NotRequired[Parameter4OrStr]
    values: NotRequired[Values1OrStr]
