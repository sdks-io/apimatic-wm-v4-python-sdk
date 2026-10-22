from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Parameter4(str, Enum):
    """To apply an enum filter based on the predefined parameter.

    | Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ITEM_AVAILABILITY_STATUS | To filter based on whether the items which are new to Walmart or existing in Walmart. |
        string |
    | DEMAND_SALES_TRENDS | Indicates the months of the year when high demand is observed for the recommended item. |
        string |"""

    ITEM_AVAILABILITY_STATUS = "ITEM_AVAILABILITY_STATUS"
    DEMAND_SALES_TRENDS = "DEMAND_SALES_TRENDS"

    __str__ = str.__str__


Parameter4OrStr: TypeAlias = Annotated[Parameter4 | str, open_enum_validator(Parameter4)]
