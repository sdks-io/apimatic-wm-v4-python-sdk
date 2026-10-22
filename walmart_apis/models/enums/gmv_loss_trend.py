from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GmvLossTrend(str, Enum):
    """gmv Loss trend"""

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


GmvLossTrendOrStr: TypeAlias = Annotated[GmvLossTrend | str, open_enum_validator(GmvLossTrend)]
