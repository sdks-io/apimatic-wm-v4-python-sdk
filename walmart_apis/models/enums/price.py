from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Price(str, Enum):
    FULL_ACCESS = "full_access"
    VIEW_ONLY = "view_only"
    NO_ACCESS = "no_access"

    __str__ = str.__str__


PriceOrStr: TypeAlias = Annotated[Price | str, open_enum_validator(Price)]
