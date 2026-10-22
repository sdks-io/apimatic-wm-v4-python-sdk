from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReplaceAll(str, Enum):
    """This is applicable only for promotions"""

    TRUE = "true"
    FALSE = "false"

    __str__ = str.__str__


ReplaceAllOrStr: TypeAlias = Annotated[ReplaceAll | str, open_enum_validator(ReplaceAll)]
