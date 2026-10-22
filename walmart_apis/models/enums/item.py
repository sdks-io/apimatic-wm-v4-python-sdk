from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Item(str, Enum):
    FULL_ACCESS = "full_access"
    VIEW_ONLY = "view_only"
    NO_ACCESS = "no_access"

    __str__ = str.__str__


ItemOrStr: TypeAlias = Annotated[Item | str, open_enum_validator(Item)]
