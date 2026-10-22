from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RequestType(str, Enum):
    WALMART_PLUS_SFF = "WALMART_PLUS_SFF"

    __str__ = str.__str__


RequestTypeOrStr: TypeAlias = Annotated[RequestType | str, open_enum_validator(RequestType)]
