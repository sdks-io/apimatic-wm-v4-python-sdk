from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WmMarket21(str, Enum):
    MX = "mx"

    __str__ = str.__str__


WmMarket21OrStr: TypeAlias = Annotated[WmMarket21 | str, open_enum_validator(WmMarket21)]
