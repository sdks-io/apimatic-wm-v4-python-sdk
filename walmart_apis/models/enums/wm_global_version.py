from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WmGlobalVersion(str, Enum):
    _3_1 = "3.1"
    """API version 3.1."""

    __str__ = str.__str__


WmGlobalVersionOrStr: TypeAlias = Annotated[WmGlobalVersion | str, open_enum_validator(WmGlobalVersion)]
