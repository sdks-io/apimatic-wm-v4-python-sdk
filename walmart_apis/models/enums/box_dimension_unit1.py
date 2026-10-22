from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BoxDimensionUnit1(str, Enum):
    """Unit of measurement for the package length, width, and height. Allowed values: IN (inches), FT (feet), CM
    (centimeters). Required when packageType is CUSTOM_PACKAGE; not required for other standard package types (e.g.,
    FEDEX_ENVELOPE, FEDEX_PAK) where dimensions are predetermined by the carrier."""

    IN = "IN"
    FT = "FT"
    CM = "CM"

    __str__ = str.__str__


BoxDimensionUnit1OrStr: TypeAlias = Annotated[BoxDimensionUnit1 | str, open_enum_validator(BoxDimensionUnit1)]
