from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BoxDimensionUnit2(str, Enum):
    IN = "IN"
    FT = "FT"
    CM = "CM"

    __str__ = str.__str__


BoxDimensionUnit2OrStr: TypeAlias = Annotated[BoxDimensionUnit2 | str, open_enum_validator(BoxDimensionUnit2)]
