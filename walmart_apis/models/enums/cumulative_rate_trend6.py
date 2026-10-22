from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CumulativeRateTrend6(str, Enum):
    """Cumulative refunds rate trend"""

    GREEN_UP = "GREEN_UP"
    GREEN = "GREEN"
    GREEN_DOWN = "GREEN_DOWN"
    YELLOW_UP = "YELLOW_UP"
    YELLOW = "YELLOW"
    YELLOW_DOWN = "YELLOW_DOWN"
    RED_UP = "RED_UP"
    RED = "RED"
    RED_DOWN = "RED_DOWN"

    __str__ = str.__str__


CumulativeRateTrend6OrStr: TypeAlias = Annotated[CumulativeRateTrend6 | str, open_enum_validator(CumulativeRateTrend6)]
