from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WmMarket1(str, Enum):
    US = "us"
    CA = "ca"
    MX = "mx"
    CL = "cl"

    __str__ = str.__str__


WmMarket1OrStr: TypeAlias = Annotated[WmMarket1 | str, open_enum_validator(WmMarket1)]
