from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CumulativeAccuracyTrend(str, Enum):
    """Cumulative ship-from location accuracy trend"""

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


CumulativeAccuracyTrendOrStr: TypeAlias = Annotated[
    CumulativeAccuracyTrend | str, open_enum_validator(CumulativeAccuracyTrend)
]
