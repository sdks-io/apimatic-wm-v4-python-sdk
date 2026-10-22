from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RequestStatus(str, Enum):
    """Status of report request. Possible values are RECEIVED, INPROGRESS, READY, ERROR."""

    RECEIVED = "RECEIVED"
    INPROGRESS = "INPROGRESS"
    READY = "READY"
    ERROR = "ERROR"

    __str__ = str.__str__


RequestStatusOrStr: TypeAlias = Annotated[RequestStatus | str, open_enum_validator(RequestStatus)]
