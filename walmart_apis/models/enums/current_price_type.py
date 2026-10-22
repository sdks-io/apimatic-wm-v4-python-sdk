from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CurrentPriceType(str, Enum):
    BASE = "BASE"
    REDUCED = "REDUCED"
    CLEARANCE = "CLEARANCE"

    __str__ = str.__str__


CurrentPriceTypeOrStr: TypeAlias = Annotated[CurrentPriceType | str, open_enum_validator(CurrentPriceType)]
