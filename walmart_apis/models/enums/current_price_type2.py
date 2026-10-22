from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CurrentPriceType2(str, Enum):
    BASE = "BASE"
    REDUCED = "REDUCED"
    SAVINGS_AMT = "SAVINGS_AMT"
    SAVINGS_PCT = "SAVINGS_PCT"
    ROLLBACK = "ROLLBACK"
    CLEARANCE = "CLEARANCE"
    LIST_PRICE = "LIST_PRICE"

    __str__ = str.__str__


CurrentPriceType2OrStr: TypeAlias = Annotated[CurrentPriceType2 | str, open_enum_validator(CurrentPriceType2)]
