from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PromotionPlacement(str, Enum):
    """Controls where discounted price is revealed to customers.<br><b style='color:green;'>Market availability: US"""

    MAP_CART = "MAP Cart"

    __str__ = str.__str__


PromotionPlacementOrStr: TypeAlias = Annotated[PromotionPlacement | str, open_enum_validator(PromotionPlacement)]
