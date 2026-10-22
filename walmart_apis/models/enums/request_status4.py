from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RequestStatus4(str, Enum):
    RECEIVED = "RECEIVED"
    INPROGRESS = "INPROGRESS"
    READY = "READY"
    ERROR = "ERROR"

    __str__ = str.__str__


RequestStatus4OrStr: TypeAlias = Annotated[RequestStatus4 | str, open_enum_validator(RequestStatus4)]
