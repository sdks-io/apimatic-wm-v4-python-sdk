from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Order1(str, Enum):
    """Sort direction."""

    ASC = "ASC"
    DESC = "DESC"

    __str__ = str.__str__


Order1OrStr: TypeAlias = Annotated[Order1 | str, open_enum_validator(Order1)]
