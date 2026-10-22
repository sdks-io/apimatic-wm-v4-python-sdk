from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status11(str, Enum):
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ENROLL | To enroll items into the program | string |
    | DISENROLL | To opt out items from the program | string |
    <br><b style='color:green;'>Market availability: US only</b>"""

    ENROLL = "ENROLL"
    DISENROLL = "DISENROLL"

    __str__ = str.__str__


Status11OrStr: TypeAlias = Annotated[Status11 | str, open_enum_validator(Status11)]
