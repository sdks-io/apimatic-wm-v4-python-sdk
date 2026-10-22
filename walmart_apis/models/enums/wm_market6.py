from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WmMarket6(str, Enum):
    MX = "mx"
    CA = "ca"
    US = "us"

    __str__ = str.__str__


WmMarket6OrStr: TypeAlias = Annotated[WmMarket6 | str, open_enum_validator(WmMarket6)]
