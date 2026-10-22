from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.parameter16 import Parameter16OrStr
from .enums.values4 import Values4OrStr


class EnumFilter4(SdkBaseModel):
    """Filter based on preset parameters and their associated values is possible with EnumFilter. No parameter should be
    repeated."""

    parameter: Optional[Parameter16OrStr] = UNSET
    """This attribute applies an enum filter based on the predefined parameter.

    | Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ITEM_AVAILABILITY_STATUS | The filters shows if an item is new or existing at Walmart. | string |
    | DEMAND_SALES_TRENDS | The months of the year when demand is high for an item. | string |"""

    values: Optional[Values4OrStr] = UNSET
    """Values correspond to the parameter used to apply filters to the response. The data in values[] are predefined. An
    OR operator is applied between multiple values.

    | Attribute | Associated parameter of enumFilter | Description | Data Type |
    | --- | ----------- | ----------- | ------- |
    | EXISTING_IN_WALMART | ITEM_AVAILABILITY_STATUS | Filters items that already exist on Walmart. | string |
    | NEW_TO_WALMART | ITEM_AVAILABILITY_STATUS | Filters items that are new to Walmart. | string |
    | JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC | DEMAND_SALES_TRENDS | Indicates the months of the
        year when high demand is expected for the recommended item. | string |"""


class EnumFilter4Dict(TypedDict):
    parameter: NotRequired[Parameter16OrStr]
    values: NotRequired[Values4OrStr]
