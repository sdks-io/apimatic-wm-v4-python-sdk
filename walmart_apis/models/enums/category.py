from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Category(str, Enum):
    APPLICATION = "APPLICATION"
    SYSTEM = "SYSTEM"
    REQUEST = "REQUEST"
    DATA = "DATA"

    __str__ = str.__str__


CategoryOrStr: TypeAlias = Annotated[Category | str, open_enum_validator(Category)]
