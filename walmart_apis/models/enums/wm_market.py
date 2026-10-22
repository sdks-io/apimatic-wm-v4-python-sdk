from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WmMarket(str, Enum):
    US = "us"

    __str__ = str.__str__


WmMarketOrStr: TypeAlias = Annotated[WmMarket | str, open_enum_validator(WmMarket)]
