from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ComparisonPriceType(str, Enum):
    """This is applicable only for promotions"""

    BASE = "BASE"

    __str__ = str.__str__


ComparisonPriceTypeOrStr: TypeAlias = Annotated[ComparisonPriceType | str, open_enum_validator(ComparisonPriceType)]
