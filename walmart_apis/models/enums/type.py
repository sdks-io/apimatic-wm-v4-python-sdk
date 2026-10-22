from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type(str, Enum):
    """Recommendation category.

    - **BUDGET**: Recommended budget adjustment (daily or total)
    - **BIDDING_STRATEGY**: Recommended change to bidding strategy"""

    BUDGET = "BUDGET"
    BIDDING_STRATEGY = "BIDDING_STRATEGY"

    __str__ = str.__str__


TypeOrStr: TypeAlias = Annotated[Type | str, open_enum_validator(Type)]
