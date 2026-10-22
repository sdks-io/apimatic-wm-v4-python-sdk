from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SellerAccountableTrend(str, Enum):
    """Seller accountable On Time Delivery rate trend"""

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


SellerAccountableTrendOrStr: TypeAlias = Annotated[
    SellerAccountableTrend | str, open_enum_validator(SellerAccountableTrend)
]
