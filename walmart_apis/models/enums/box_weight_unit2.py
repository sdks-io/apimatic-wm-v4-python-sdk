from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BoxWeightUnit2(str, Enum):
    LB = "LB"
    KG = "KG"
    OZ = "OZ"

    __str__ = str.__str__


BoxWeightUnit2OrStr: TypeAlias = Annotated[BoxWeightUnit2 | str, open_enum_validator(BoxWeightUnit2)]
