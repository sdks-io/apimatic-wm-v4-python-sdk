from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Parameter16(str, Enum):
    """This attribute applies an enum filter based on the predefined parameter.

    | Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ITEM_AVAILABILITY_STATUS | The filters shows if an item is new or existing at Walmart. | string |
    | DEMAND_SALES_TRENDS | The months of the year when demand is high for an item. | string |"""

    ITEM_AVAILABILITY_STATUS = "ITEM_AVAILABILITY_STATUS"
    DEMAND_SALES_TRENDS = "DEMAND_SALES_TRENDS"

    __str__ = str.__str__


Parameter16OrStr: TypeAlias = Annotated[Parameter16 | str, open_enum_validator(Parameter16)]
