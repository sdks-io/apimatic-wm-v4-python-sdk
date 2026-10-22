from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FeedStatus(str, Enum):
    """Can be one of the following: RECEIVED, INPROGRESS, PROCESSED, or ERROR"""

    RECEIVED = "RECEIVED"
    INPROGRESS = "INPROGRESS"
    PROCESSED = "PROCESSED"
    ERROR = "ERROR"

    __str__ = str.__str__


FeedStatusOrStr: TypeAlias = Annotated[FeedStatus | str, open_enum_validator(FeedStatus)]
