from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Name(str, Enum):
    """Name of the AddOn type."""

    SIGNATURE = "SIGNATURE"
    INSURANCE = "INSURANCE"

    __str__ = str.__str__


NameOrStr: TypeAlias = Annotated[Name | str, open_enum_validator(Name)]
