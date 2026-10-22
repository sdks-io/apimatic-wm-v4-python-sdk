from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PriceDisplayCodes1(str, Enum):
    """This is applicable only for promotions"""

    CART = "CART"
    CHECKOUT = "CHECKOUT"

    __str__ = str.__str__


PriceDisplayCodes1OrStr: TypeAlias = Annotated[PriceDisplayCodes1 | str, open_enum_validator(PriceDisplayCodes1)]
