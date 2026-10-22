from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ComparisonPriceType2(str, Enum):
    BASE = "BASE"
    REDUCED = "REDUCED"
    SAVINGS_AMT = "SAVINGS_AMT"
    SAVINGS_PCT = "SAVINGS_PCT"
    ROLLBACK = "ROLLBACK"
    CLEARANCE = "CLEARANCE"
    LIST_PRICE = "LIST_PRICE"

    __str__ = str.__str__


ComparisonPriceType2OrStr: TypeAlias = Annotated[ComparisonPriceType2 | str, open_enum_validator(ComparisonPriceType2)]
