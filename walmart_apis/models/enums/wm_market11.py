from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WmMarket11(str, Enum):
    MX = "mx"
    CA = "ca"
    CL = "cl"

    __str__ = str.__str__


WmMarket11OrStr: TypeAlias = Annotated[WmMarket11 | str, open_enum_validator(WmMarket11)]
