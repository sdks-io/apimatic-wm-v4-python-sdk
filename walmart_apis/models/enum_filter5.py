from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.parameter20 import Parameter20OrStr
from .enums.values5 import Values5OrStr


class EnumFilter5(SdkBaseModel):
    """Filter based on preset parameters and their associated values is possible with EnumFilter. No parameter should be
    repeated. <br><b style='color:green;'>Market availability: US only</span></b>"""

    parameter: Optional[Parameter20OrStr] = UNSET
    """Used to apply an enum filter based on a predefined parameter.

    | Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ITEM_AVAILABILITY_STATUS | Filters items based on whether they are new to Walmart or already exist on Walmart. |
        string |
    | DEMAND_SALES_TRENDS | Indicates the months of the year when high demand is observed for the recommended item. |
        string |"""

    values: Optional[Values5OrStr] = UNSET
    """Values correspond to the parameter used to apply filters to the response. The data in values[] are predefined. An
    OR operator is used between the values.

    | Attribute | Associated parameter of enumFilter | Description | Data Type |
    | --- | --- | --- | --- |
    | EXISTING_IN_WALMART | ITEM_AVAILABILITY_STATUS | Filters items that already exist on Walmart. | string |
    | NEW_TO_WALMART | ITEM_AVAILABILITY_STATUS | Filters items that are new to Walmart. | string |
    | JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC | DEMAND_SALES_TRENDS | Indicates the months of the
        year when high demand is observed for the recommended item. | string |"""


class EnumFilter5Dict(TypedDict):
    parameter: NotRequired[Parameter20OrStr]
    values: NotRequired[Values5OrStr]
