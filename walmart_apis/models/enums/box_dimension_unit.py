from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BoxDimensionUnit(str, Enum):
    """Unit of measurement for the package length, width, and height. Allowed values: IN (inches), FT (feet), CM
    (centimeters)."""

    IN = "IN"
    FT = "FT"
    CM = "CM"

    __str__ = str.__str__


BoxDimensionUnitOrStr: TypeAlias = Annotated[BoxDimensionUnit | str, open_enum_validator(BoxDimensionUnit)]
