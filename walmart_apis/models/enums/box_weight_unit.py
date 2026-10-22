from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BoxWeightUnit(str, Enum):
    """Unit of measurement for the package weight. Allowed values: LB (pounds), KG (kilograms), OZ (ounces)."""

    LB = "LB"
    KG = "KG"
    OZ = "OZ"

    __str__ = str.__str__


BoxWeightUnitOrStr: TypeAlias = Annotated[BoxWeightUnit | str, open_enum_validator(BoxWeightUnit)]
