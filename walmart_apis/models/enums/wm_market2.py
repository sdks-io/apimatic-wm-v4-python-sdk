from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WmMarket2(str, Enum):
    US = "US"
    CA = "CA"
    MX = "MX"
    CL = "CL"

    __str__ = str.__str__


WmMarket2OrStr: TypeAlias = Annotated[WmMarket2 | str, open_enum_validator(WmMarket2)]
