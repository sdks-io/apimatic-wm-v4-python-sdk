from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ClaimsGroup(str, Enum):
    OPEN = "OPEN"
    ACTION_NEEDED = "ACTION_NEEDED"
    CLOSED = "CLOSED"

    __str__ = str.__str__


ClaimsGroupOrStr: TypeAlias = Annotated[ClaimsGroup | str, open_enum_validator(ClaimsGroup)]
