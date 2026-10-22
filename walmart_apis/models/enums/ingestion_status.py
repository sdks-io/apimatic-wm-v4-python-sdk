from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IngestionStatus(str, Enum):
    """Can be one of the following: DATA_ERROR, SYSTEM_ERROR, TIMEOUT_ERROR, or INPROGRESS"""

    INPROGRESS = "INPROGRESS"
    SUCCESS = "SUCCESS"
    DATA_ERROR = "DATA_ERROR"
    SYSTEM_ERROR = "SYSTEM_ERROR"
    TIMEOUT_ERROR = "TIMEOUT_ERROR"

    __str__ = str.__str__


IngestionStatusOrStr: TypeAlias = Annotated[IngestionStatus | str, open_enum_validator(IngestionStatus)]
