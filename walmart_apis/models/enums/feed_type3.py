from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FeedType3(str, Enum):
    PROGRAM_ACTIONS = "PROGRAM_ACTIONS"

    __str__ = str.__str__


FeedType3OrStr: TypeAlias = Annotated[FeedType3 | str, open_enum_validator(FeedType3)]
