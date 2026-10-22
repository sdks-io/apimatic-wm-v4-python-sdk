from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Name7(str, Enum):
    """Name of the add-on type."""

    SIGNATURE = "SIGNATURE"
    INSURANCE = "INSURANCE"

    __str__ = str.__str__


Name7OrStr: TypeAlias = Annotated[Name7 | str, open_enum_validator(Name7)]
