from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Values5(str, Enum):
    """Values correspond to the parameter used to apply filters to the response. The data in values[] are predefined. An
    OR operator is used between the values.

    | Attribute | Associated parameter of enumFilter | Description | Data Type |
    | --- | --- | --- | --- |
    | EXISTING_IN_WALMART | ITEM_AVAILABILITY_STATUS | Filters items that already exist on Walmart. | string |
    | NEW_TO_WALMART | ITEM_AVAILABILITY_STATUS | Filters items that are new to Walmart. | string |
    | JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC | DEMAND_SALES_TRENDS | Indicates the months of the
        year when high demand is observed for the recommended item. | string |"""

    EXISTING_IN_WALMART = "EXISTING_IN_WALMART"
    NEW_TO_WALMART = "NEW_TO_WALMART"
    MOST_SEARCHED_FOR = "MOST_SEARCHED_FOR"
    BEST_SELLERS = "BEST_SELLERS"
    DEAL_ITEMS = "DEAL_ITEMS"
    JAN = "JAN"
    FEB = "FEB"
    MAR = "MAR"
    APR = "APR"
    MAY = "MAY"
    JUN = "JUN"
    JUL = "JUL"
    AUG = "AUG"
    SEP = "SEP"
    OCT = "OCT"
    NOV = "NOV"
    DEC = "DEC"

    __str__ = str.__str__


Values5OrStr: TypeAlias = Annotated[Values5 | str, open_enum_validator(Values5)]
