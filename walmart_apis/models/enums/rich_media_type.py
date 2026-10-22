from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RichMediaType(str, Enum):
    IMAGES360 = "IMAGES360"
    VIDEO = "VIDEO"

    __str__ = str.__str__


RichMediaTypeOrStr: TypeAlias = Annotated[RichMediaType | str, open_enum_validator(RichMediaType)]
