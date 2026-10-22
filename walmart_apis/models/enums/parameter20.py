from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Parameter20(str, Enum):
    """Used to apply an enum filter based on a predefined parameter.

    | Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ITEM_AVAILABILITY_STATUS | Filters items based on whether they are new to Walmart or already exist on Walmart. |
        string |
    | DEMAND_SALES_TRENDS | Indicates the months of the year when high demand is observed for the recommended item. |
        string |"""

    ITEM_AVAILABILITY_STATUS = "ITEM_AVAILABILITY_STATUS"
    DEMAND_SALES_TRENDS = "DEMAND_SALES_TRENDS"

    __str__ = str.__str__


Parameter20OrStr: TypeAlias = Annotated[Parameter20 | str, open_enum_validator(Parameter20)]
