from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Category1(str, Enum):
    """Category classifying the origin of the error."""

    APPLICATION = "APPLICATION"
    SERVICE = "SERVICE"
    REQUEST = "REQUEST"
    DATA = "DATA"

    __str__ = str.__str__


Category1OrStr: TypeAlias = Annotated[Category1 | str, open_enum_validator(Category1)]
