from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status1(str, Enum):
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ENROLL | To enroll items into the program | string |
    | DISENROLL | To opt out items from the program | string |"""

    ENROLL = "ENROLL"
    DISENROLL = "DISENROLL"

    __str__ = str.__str__


Status1OrStr: TypeAlias = Annotated[Status1 | str, open_enum_validator(Status1)]
