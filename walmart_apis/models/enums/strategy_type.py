from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StrategyType(str, Enum):
    """Strategy type supported for markets is Buy Box Price(for us and mx), External Price(for US, MX and CA),
    Competitive Price(for us and mx).<br><b style="color:green;">Market availability: US | CA | MX</b>"""

    BUY_BOX_PRICE = "Buy Box Price"
    EXTERNAL_PRICE = "External Price"
    COMPETITIVE_PRICE = "Competitive Price"

    __str__ = str.__str__


StrategyTypeOrStr: TypeAlias = Annotated[StrategyType | str, open_enum_validator(StrategyType)]
