from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DemandSalesTrends(str, Enum):
    """Indicates the months of the year when high demand is observed for the recommended item. The sequence of month is
    in the decreasing order of the high demand. The values are comma separated.

    | Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC | Months of the year. | string |"""

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


DemandSalesTrendsOrStr: TypeAlias = Annotated[DemandSalesTrends | str, open_enum_validator(DemandSalesTrends)]
