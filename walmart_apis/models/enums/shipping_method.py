from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShippingMethod(str, Enum):
    """shipping methods used to calculate these metrics"""

    ALL_METHODS = "ALL_METHODS"
    TWO_DAY = "TWO_DAY"
    ONE_DAY = "ONE_DAY"

    __str__ = str.__str__


ShippingMethodOrStr: TypeAlias = Annotated[ShippingMethod | str, open_enum_validator(ShippingMethod)]
