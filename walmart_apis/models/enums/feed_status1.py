from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FeedStatus1(str, Enum):
    RECEIVED = "RECEIVED"
    INPROGRESS = "INPROGRESS"
    PROCESSED = "PROCESSED"
    ERROR = "ERROR"

    __str__ = str.__str__


FeedStatus1OrStr: TypeAlias = Annotated[FeedStatus1 | str, open_enum_validator(FeedStatus1)]
