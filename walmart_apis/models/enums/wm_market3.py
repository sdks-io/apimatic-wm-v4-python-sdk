from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WmMarket3(str, Enum):
    US = "us"
    MX = "mx"

    __str__ = str.__str__


WmMarket3OrStr: TypeAlias = Annotated[WmMarket3 | str, open_enum_validator(WmMarket3)]
