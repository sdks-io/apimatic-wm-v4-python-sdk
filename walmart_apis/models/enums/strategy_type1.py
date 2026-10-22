from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StrategyType1(str, Enum):
    """Strategy type supported for markets is Buy Box Price(for us and mx),External Price(for us and mx, ca),Competitive
    Price(for us and mx).<br><b style="color:green;">Market availability: US | CA | MX</b>"""

    BUY_BOX_PRICE = "Buy Box Price"
    EXTERNAL_PRICE = "External Price"
    COMPETITIVE_PRICE = "Competitive Price"

    __str__ = str.__str__


StrategyType1OrStr: TypeAlias = Annotated[StrategyType1 | str, open_enum_validator(StrategyType1)]
