from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CumulativeRateTrend8(str, Enum):
    """Cumulative rate of orders cancelled trend"""

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


CumulativeRateTrend8OrStr: TypeAlias = Annotated[CumulativeRateTrend8 | str, open_enum_validator(CumulativeRateTrend8)]
