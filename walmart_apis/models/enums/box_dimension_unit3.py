from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BoxDimensionUnit3(str, Enum):
    """The unit of measurement for the package length, width, and height. Allowed values: IN (inches), FT (feet), CM
    (centimeters).

    <b style="color: green;">Market availability: Global</b>"""

    IN = "IN"
    FT = "FT"
    CM = "CM"

    __str__ = str.__str__


BoxDimensionUnit3OrStr: TypeAlias = Annotated[BoxDimensionUnit3 | str, open_enum_validator(BoxDimensionUnit3)]
