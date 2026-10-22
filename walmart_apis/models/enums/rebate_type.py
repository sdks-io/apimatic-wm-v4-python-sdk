from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RebateType(str, Enum):
    AMOUNT = "AMOUNT"
    PRODUCT = "PRODUCT"

    __str__ = str.__str__


RebateTypeOrStr: TypeAlias = Annotated[RebateType | str, open_enum_validator(RebateType)]
