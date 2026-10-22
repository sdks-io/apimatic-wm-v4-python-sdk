from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FreeShipping1(str, Enum):
    """Indicates if the shipping is free for a recommended item which is a buy box winner."""

    YES = "YES"
    NO = "NO"

    __str__ = str.__str__


FreeShipping1OrStr: TypeAlias = Annotated[FreeShipping1 | str, open_enum_validator(FreeShipping1)]
