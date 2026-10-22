from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BoxWeightUnit3(str, Enum):
    """The unit of measurement for the package weight. Allowed values: LB (pounds), KG (kilograms), OZ (ounces).

    <b style="color: green;">Market availability: Global</b>"""

    LB = "LB"
    KG = "KG"
    OZ = "OZ"

    __str__ = str.__str__


BoxWeightUnit3OrStr: TypeAlias = Annotated[BoxWeightUnit3 | str, open_enum_validator(BoxWeightUnit3)]
