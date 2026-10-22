from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type2(str, Enum):
    """Indicates the error type."""

    DATA_ERROR = "DATA_ERROR"
    SYSTEM_ERROR = "SYSTEM_ERROR"
    TIMEOUT_ERROR = "TIMEOUT_ERROR"

    __str__ = str.__str__


Type2OrStr: TypeAlias = Annotated[Type2 | str, open_enum_validator(Type2)]
