from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ComparisonPriceType6(str, Enum):
    """<br><b style='color:green;'>Market availability: Global</b>"""

    BASE = "BASE"
    REDUCED = "REDUCED"
    SAVINGS_AMT = "SAVINGS_AMT"
    SAVINGS_PCT = "SAVINGS_PCT"
    ROLLBACK = "ROLLBACK"
    CLEARANCE = "CLEARANCE"
    LIST_PRICE = "LIST_PRICE"

    __str__ = str.__str__


ComparisonPriceType6OrStr: TypeAlias = Annotated[ComparisonPriceType6 | str, open_enum_validator(ComparisonPriceType6)]
